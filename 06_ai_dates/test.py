import requests
import json
# Usar la API de GPT-4o de OpenAI

api_key = "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"
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