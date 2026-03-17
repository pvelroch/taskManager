# import os
# from typing import List

# from dotenv import load_dotenv
# from openai import OpenAI


# load_dotenv()


# def create_simple_task(description: str) -> List[str]:
#     """Genera una lista simple de subtareas a partir de una descripción."""
#     api_key = os.getenv("OPENAI_API_KEY")

#     if not api_key:
#         # Fallback local si no hay API key
#         parts = [p.strip().capitalize() for p in description.replace(" y ", ",").split(",") if p.strip()]
#         return parts if parts else [description.strip().capitalize()]

#     client = OpenAI(api_key=api_key)

#     response = client.responses.create(
#         model="gpt-4.1-mini",
#         input=(
#             "Convierte esta tarea en 3 a 5 subtareas cortas en español. "
#             "Responde solo con líneas con viñetas '-'.\n\n"
#             f"Tarea: {description}"
#         ),
#     )

#     text = response.output_text.strip()
#     lines = [line.strip("-• \t") for line in text.splitlines() if line.strip()]
#     return lines if lines else [description.strip().capitalize()]


import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Load environment variables from .env file

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_simple_task(description):

    if not client.api_key:
        return ["OpenAI API key is not set. Please set it in the .env file."]

    try:
        prompt = f"""Desglosa la siguiente tarea completa en una lista de 3 a 5 subtareas simples y accionables.

        Tarea: {description}

        Formato de respuesta:
        1. Subtarea 1
        2. Subtarea 2
        ...

        Responde solo con la lista de subtareas, sin texto adicional."""

        params = {
            "model": "gpt-5",
            "messages": [
                {"role": "system", "content": "Eres un asistente útil que desglosa tareas complejas en subtareas simples."},
                {"role": "user", "content": prompt}
            ],
            "max_completions_tokens": 300,
            "verbosity": "medium",
            "reasoning_effort": "minimal"
        }

        response = client.chat.completions.create(**params)

        content = response.choices[0].message.content.strip().splitlines()

        subtasks = [line.strip() for line in content if line.strip()]

        return subtasks

    except Exception as e:
        return [f"An error occurred while creating the task: {str(e)}"]

