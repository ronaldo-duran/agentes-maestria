import os
 
from dotenv import load_dotenv
from strands import Agent, tool
from strands.models.gemini import GeminiModel
from strands_tools import calculator, http_request, file_write, file_read
 
load_dotenv()
 
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("Falta GEMINI_API_KEY en el entorno o en el archivo .env")
 
tavily_api_key = os.getenv("TAVILY_API_KEY")
if not tavily_api_key:
    raise ValueError("Falta TAVILY_API_KEY en el entorno o en el archivo .env")
 
model = GeminiModel(
    model_id=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
    client_args={"api_key": gemini_api_key},
)
 
@tool
def busqueda_papers(busqueda: str) -> dict:
    """
    Dado un promt de buqueda usa tavily par encontrar papers relacionados con el promt
 
    Args:
        busqueda (str): El prompt de búsqueda para encontrar papers relacionados
    """
 
    # To install: pip install tavily-python
    from tavily import TavilyClient
    client = TavilyClient(tavily_api_key)
    response = client.search(
        query=busqueda,
        include_answer=True,
        search_depth="advanced",
        start_date="2024-01-01",
        include_raw_content="markdown",
        include_domains=["arxiv.org"]
    )
    return response
 
@tool
def search_agent(consulta: str) -> list[dict]:
    """
    Procesa y respoinde a las consultas de investigacion de papers.
   
    Args:
        consulta (str): Una consulta de investigación requiriendo fuentes de papers
    Returns:
        Una lista con los resultados de la consulta, cada elemento de la lista es un diccionari con la sigueinte estructura
            -url: la url del paper,
            -doi: el doi del paper,
            -title: el titulo del paper,
            -abstract: el resumen del paper,
   
 
    """
    BUSQUEDA_SYSTEM_PROMPT = """
    Eres un asistente para estudiantes de maestria que deben encotnrar paper para construir su estado dle arte.
    Enfocate soo en proveer informacion actual y bien organizada para responder a la solucitud del estudiante.
    Siempre cita las fuentes si es posible.
    """
    del BUSQUEDA_SYSTEM_PROMPT
 
    response = busqueda_papers(consulta)
    resultados = response.get("results", [])
 
    papers = []
    for item in resultados:
        papers.append(
            {
                "url": item.get("url"),
                "doi": item.get("doi"),
                "title": item.get("title"),
                "abstract": item.get("content"),
            }
        )
 
    return papers
 
 
@tool
def bibtext_agent(papers_list: list[dict], solicitud_usuario: str, score_filtro: float) -> str:
    """
    Procesa la solit
    Recibe una lista de papers, crea o actualiza un archivo bibtex con la información de los papers.
 
    Args:
        papers_list: Una lista con los resultados de la consulta, cada elemento de la lista es un diccionario con la siguiente estructura
            - url: la url del paper
            - doi: el doi del paperS
            - title: el titulo del paper
            - abstract: el resumen del paper
            - score: score de relevancia la busqueda en tavily
        solicitud_usuario: La solicitud del usuario
        score_filtro: El score minimo para filtrar los papers
    Returns:
        La ruta del archivo bibtex creado
    """
 
    BIBTEX_SYSTEM_PROMPT = """
    Eres un asistente para estudiantes de maestría que deben organizar en un archivo sus papers en formato bibtex.
    Enfocate en crear o actualizar un archivo actual llamado referencias.bib donde cada elemento es una referencia en formato bibtext.
    Filtra los resultados por el scoring dado por el usuario.
    Antes de escribir los resultados, SI EXISTE el archivo, leelo y decide si tienes que actualizarlo o no.
    responde con la ruta del archivo bibtex creado o actualizado usando el tool file_write.
    Este es un ejemplo del formato
    @article{jovanovic2020chatbots,
    author    = {Jovanovi{\'c}, Milica and Baez, Marcos and Casati, Fabio},
    title     = {Chatbots as Conversational Healthcare Services},
    journal   = {IEEE Internet Computing},
    year      = {2020},
    url       = {https://arxiv.org/pdf/2011.03969},
    keywords  = {chatbots, healthcare, conversational agents},
    note      = {Scoring: 0.85}
 
    """
 
    agent = Agent(
        model=model,
        tools=[file_write],
        system_prompt=BIBTEX_SYSTEM_PROMPT,
    )
 
    prompt = (
        "Solicitud del usuario: "
        f"{solicitud_usuario}\n\n"
        f"Score minimo de filtro: {score_filtro}\n\n"
        "Lista de papers:\n"
        f"{papers_list}"
    )
    return agent(prompt)
 
@tool
def deep_reasearch_agent(consulta: str) -> str:
    """
    Procesa la solicitud de hacer un deep research apartir de las refrecnia creadas de un aerchivo bibtex
    recibe el nombre del archiv bibtext, extrae la URL del paper y genera un resumen para que lo entienda un niño
 
    Args:
        consulta: el nombre del archivo bibtex con las referencias de los papers
 
    Returns:
        el resultado del deep research
   
    """
    SYSTEM_PROMPT="""
    Eres un investigador que lee paper y te encargas de generar resumenes orientados a que niñls puedan entenderlos.
    """
   
    agent = Agent(
        model=model,
        tools=[file_write,http_request, file_read],
        system_prompt=SYSTEM_PROMPT,
    )
    return agent(f"lee el archivo {consulta} y por cada artículo, usa la url para extraer el paper y generar un resumen por cada uno en extension markdown. guardalo en una carpeta que se llame resumenes")
 
 
@tool
def paper_generator_agent(consulta: str) -> str:
    """
    Procesa la solicitud de generar un paper apartir de las refrecnia creadas de un aerchivo bibtex
    """
    SYSTEM_PROMPT="""
    Eres un investigador que lee paper y te encargas de generar un paper de revisión sistemática a partir de las referencias de un archivo bibtex.
    """
   
    agent = Agent(
        model=model,
        tools=[file_write,http_request, file_read],
        system_prompt=SYSTEM_PROMPT,
    )
    return agent("lee el archivo referencias.bib y genera un paper de revisión sistemática a partir de las referencias, el paper debe estar en formato markdown y debe tener una estructura clara con introducción, metodología, resultados y conclusión. guardalo con el nombre paper_revisión_sistemática.md")
 
 
ORQUESTADOR_SYSTEM_PROMPT = """
    Eres un asisten que enruta consultas para agentes especializados:
    - Para consultas de papers e información factual -> utiliza el tool `search_agent`
    - Para preguntas simples que no requieren agentes con conocimientos especializados -> Responde directamente al usuario
    - Para solicitudes de guardar los resultados de la consulta en un archivo bibtex -> utiliza el tool `bibtext_agent`
    - Para realizar deep research sobre los resultados de la consulta -> utiliza el tool `deep_research_agent` y necesita el nombre del archivo bibtex generado por el tool `bibtext_agent`
    - Para realizar papers sobre temas de investigación -> utiliza el tool `paper_generator` y necesita las instrucciones para generar el paper.
    Siempre selecciona el tool mas adecuado basado en la consulta del usuario.
"""
 
 
agent_orquestador = Agent(
    model=model,
    tools=[search_agent,bibtext_agent,busqueda_papers,deep_reasearch_agent, file_write, paper_generator_agent],
    system_prompt=ORQUESTADOR_SYSTEM_PROMPT,
)
 
if __name__ == "__main__":
    print("Chat iniciado. Escribe 'salir' para terminar.\n")
    while True:
        user_input = input("Tú: ").strip()
        if user_input.lower() in ("salir", "exit", "quit"):
            print("¡Hasta luego!")
            break
        if not user_input:
            continue
        response = agent_orquestador(user_input)