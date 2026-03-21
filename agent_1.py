import os

from dotenv import load_dotenv
from strands import Agent
from strands.models.bedrock import BedrockModel
from strands_tools import calculator, http_request

load_dotenv()

# Configura la API key de Bedrock como bearer token
os.environ["AWS_BEARER_TOKEN_BEDROCK"] = os.getenv("AWS_BEARER_TOKEN_BEDROCK", "")

model = BedrockModel(
    model_id="us.anthropic.claude-sonnet-4-20250514-v1:0",
    region_name="us-east-1",
)

agent = Agent(
    model=model,
    tools=[calculator, http_request],
    system_prompt="Eres un asistente útil y amigable.",
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
        response = agent(user_input)
        print(f"\nAgente: {response}\n")
