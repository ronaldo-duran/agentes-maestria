import os

from dotenv import load_dotenv
from strands import Agent, tool
from strands.models.bedrock import BedrockModel
from strands_tools import calculator, http_request, file_write
from tavily import TavilyClient


load_dotenv()

# Configura la API key de Bedrock como bearer token
os.environ["AWS_BEARER_TOKEN_BEDROCK"] = os.getenv("AWS_BEARER_TOKEN_BEDROCK", "")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")

@tool
def busqueda_papers(busqueda: str) -> dict:
    """
    Dado prompt de búsqueda usa  tavily para encontrar papers relacionados a al prompt enviado

    Args:
        busqueda: str tema a buscar
    """

    # To install: pip install tavily-python

    client = TavilyClient(TAVILY_API_KEY)    
    response = client.search(
        query=busqueda,
        include_answer="advanced",
        search_depth="advanced",
        start_date="2024-01-01",
        include_raw_content="markdown",
        include_domains=["arxiv.org"]
    )
    return response

@tool
def search_agent(consulta: str) -> list[dict]:
    """
    Procesa y responde a las consultas de investigación de papers

    Args:
        busqueda: una consulta de investigación requiriendo fuentes de papers
    Returns:
        Una lista con los resultados de la consulta, cada elemento de la lista es un diccionario con la siguiente estrctura:
            - url: url del paper encontrado
            - doi: doi del paper encontrado
            - title: titulo del paper encontrado
            - abstract: resumen del paper encontrado
            - score: score de relevancia la busqueda en tavily
    """
    BUSQUEDA_SYSTEM_PROMPT = """Eres un asistente para estudiantes de maestría que deben encontrar papers para construir su estado del arte.
    Enfocate solo en proveer información actual y bien organizada para responder la solicitud del estudiante.
    Siempre cita las fuentes de ser posible."""

    agent = Agent(
        model=model,
        tools=[busqueda_papers],
        system_prompt=BUSQUEDA_SYSTEM_PROMPT,
    )

    response = agent(consulta)
    return response

@tool
def bibtext_agent(papers_list: list[dict],  score_filtro:float=0.5) -> str:
  """
  Recibe una lista de papers, creo o actualiza un archivo bibtex con la información de los papers.

  Args:
      papers_list: Una lista con los resultados de la consulta, cada elemento de la lista es un diccionario con la siguiente estructura
        - url: la url del paper
        - doi: el doi del paper
        - title: el titulo del paper
        - abstract: el resumen del paper
        - score: score de relevancia la busqueda en tavily
      score_filtro: El score minimo para filtrar los papers
  Returns:
      La ruta del archivo bibtex creado
  """

  BIBTEX_SYSTEM_PROMPT="""Eres un asistente para estudiantes de maestría que deben organizar en un archivo sus papers en formato bibtex. 
  enfocate en crear o actualizar un archivo llamado referencias.json donde cada elemento es una referencia en formato bibtex.
  Filtra los resultados por el scoring dado por el usuario.
  Responde con la ruta del archivo creado o actualizado usando el tool file_write.
  """

  agent=Agent(
    model=model,
    tools=[file_write],
    system_prompt=BIBTEX_SYSTEM_PROMPT
  )

  return agent(papers_list, score_filtro)

model = BedrockModel(
    model_id="global.anthropic.claude-opus-4-6-v1",
    region_name="us-east-1",
)

ORQUESTADOR_SYSTEM_PROMPT = """
Eres un asistente que enruta consultas para agentes especializados:
- Para consultas de papers e información actual -> utiliza el tool 'search_agent'
- Para guardar los resultados de la consulta en un archivo bibtex -> utiliza el tool 'bibtext_agent'
- Para consultas simples que no requieren agentes con conocimiento especializado -> responde directamente al usuario

Siempre selecciona el tool más adecuado para responder a la consulta del usuario.
"""

agentOrquestador = Agent(
    model=model,
    tools=[search_agent, bibtext_agent,file_write],
    system_prompt=ORQUESTADOR_SYSTEM_PROMPT,
)

if __name__ == "__main__":
    print("Chat iniciado. Escribe 'salir' para terminar.\n")
    while True:
        user_input = input("\nTú: ").strip()
        if user_input.lower() in ("salir", "exit", "quit"):
            print("¡Hasta luego!")
            break
        if not user_input:
            continue
        response = agentOrquestador(user_input)