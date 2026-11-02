import os

from dotenv import load_dotenv
from strands import Agent
from strands.models.gemini import GeminiModel
from strands_tools import calculator, http_request

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("Falta GEMINI_API_KEY en el entorno o en el archivo .env")

model = GeminiModel(
    model_id=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
    client_args={"api_key": gemini_api_key},
)

agent = Agent(
    model=model,
    tools=[calculator, http_request],
    system_prompt="Eres un asistente útil y amigable.",
)

if __name__ == "__main__":
    while True:
        input_str = input("Escribe tu pregunta (o 'salir' para terminar): ")
        if input_str.lower() == "salir":
            break
        response = agent(input_str)
