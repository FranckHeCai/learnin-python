# Peticiones sin dependencias (dificil y sin dependencias)

# pip install requests --system-break-packages | En el caso de usar MacOs, para indicar  que lo instala a nivel de sistema

import urllib.request
import json
import os
os.system('clear')

# Lo que hace este codigo es como abrir el navegador y poner la URL
# y luego leer el resultado (HTML, JSON, XML etc) y luego procesarlo
# try:
#   api_posts = "https://jsonplaceholder.typicode.com/posts/"
#   response = urllib.request.urlopen(api_posts)
#   data = response.read()
#   json_data = json.loads(data.decode('utf-8'))
#   print(json_data)
#   response.close()
# except urllib.error.URLError as e:
#   print(f"Error fetching data: {e}")

# Peticiones con dependencia (requests)
import requests

api_posts = "https://jsonplaceholder.typicode.com/posts/"

print("\nGET:")
response = requests.get(api_posts)
json = response.json()
print(json[0])

# Un POST
print("\nPOST:")
api_posts = "https://jsonplaceholder.typicode.com/posts/"
input = {
  "title": "Yoasobi",
  "body": "Yoasobi is a Japanese music duo",
  "userId": 1
}

# response = requests.port(api_posts, json = {
#   "title": "Yoasobi",
#   "body": "Yoasobi is a Japanese music duo",
#   "userId": 1
# })

response = requests.post(api_posts, json = input)
print(response.status_code)
print(response.json())

try:
  response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={
      "title": "foo",
      "body": "bar",
      "userId": 1
    })
  print(response.status_code)
except requests.exceptions.RequestException as e:
  print(f"Error en la solicitud: {e}")

# Un PUT
print("\nPUT:")
try:
  response = requests.put(
    "https://jsonplaceholder.typicode.com/posts",
    json={
      "title": "foo",
      "body": "bar",
      "userId": 1
    })
  print(response.status_code)
except requests.exceptions.RequestException as e:
  print(f"Error en la solicitud: {e}")

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

# Llamar a la API de DeepSeek

deepseek_api_key = "sk-bfd38c3c6e0c4b7cb04a7507dd8338e2"
def get_gpt4o_response(api_key, prompt):

  url = "	https://api.deepseek.com/v1/chat/completions"
  headers = {
    "Content-Type": "application/json", 
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "deepseek-chat",
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

response = get_gpt4o_response(deepseek_api_key, "¿Cuál es la capital de Francia?")

print(json.dumps(response, indent = 2))