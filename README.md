# Agentes Strands con Gemini

Aplicación de agentes IA construida con [Strands Agents SDK](https://strandsagents.com/) usando Gemini de Google como proveedor de modelo.

## Requisitos previos

- Python 3.10+
- Una API key de Gemini de [Google AI Studio](https://aistudio.google.com/apikey)

## Instalación

1. Crea un entorno virtual:

```bash
python -m venv .venv
```

2. Activa el entorno virtual según tu sistema operativo:

**macOS / Linux:**
```bash
source .venv/bin/activate
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Copia `.env.example` como `.env` y configura:

```env
GEMINI_API_KEY=tu_api_key_de_google_ai_studio
GEMINI_MODEL=gemini-2.5-flash
TAVILY_API_KEY=tu_api_key_de_tavily
```

`GEMINI_MODEL` es opcional. Puedes cambiarlo por otro modelo disponible en tu cuenta; el valor predeterminado está pensado para el nivel gratuito.
 