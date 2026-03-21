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

model = BedrockModel(
    model_id="global.anthropic.claude-opus-4-6-v1",
    region_name="us-east-1",
)

agent = Agent(
    model=model,
    tools=[busqueda_papers,file_write],
    system_prompt="Eres un asistente para estudiantes de maestría que deben sufrir mucho encontrando el estado del arte para su trabajo de grado.",
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
        response = agent(user_input)