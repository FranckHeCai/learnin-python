import requests
from dotenv import load_dotenv
load_dotenv()
import os
openai_api_key = os.getenv("OPENAI_KEY")
deepseek_api_key = os.getenv("DEEPSEEK_KEY")
class AI_API:
    def __init__(self, url, model, api_key):
      self.__url = url
      self.__model = model
      self.__api_key = api_key


    def get_response(self, prompt):
      headers = {
        "Content-Type": "application/json", 
        "Authorization": f"Bearer {self.__api_key}"
      }
      data = {
        "model": self.__model,
        "messages": [{"role": "user", "content": prompt}]
      }
      try:
        response = requests.post(self.__url, json = data, headers = headers)
        print(response.status_code)
      except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
      
      return response.json()
    
openAI_api = AI_API("https://api.openai.com/v1/chat/completions", "gpt-4o-mini", openai_api_key)
response = openAI_api.get_response("¿Cuál es la capital de Francia?")
print(response)