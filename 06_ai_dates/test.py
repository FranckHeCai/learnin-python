import requests
import json
import os
# Usar la API de GPT-4o de OpenAI
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_KEY")
def get_gpt4o_response(api_key, prompt):

  url = "https://api.openai.com/v1/chat/completions"
  headers = {
    "Content-Type": "application/json", 
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": prompt}]
  }

  try:
    response = requests.post(
      url,
      headers = headers,
      json = data
  )
    print(response.status_code)
  except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")

  return response.json()

response = get_gpt4o_response(api_key, "¿Cuál es la capital de Francia?")

print(json.dumps(response, indent = 2))