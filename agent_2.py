import os

from dotenv import load_dotenv
from strands import Agent, tool
from strands.models.gemini import GeminiModel
from strands_tools import calculator, http_request, file_write
from tavily import TavilyClient


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("Falta GEMINI_API_KEY en el entorno o en el archivo .env")

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

model = GeminiModel(
    model_id=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
    client_args={"api_key": gemini_api_key},
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