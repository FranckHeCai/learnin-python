import requests
# def get_weather(temp):
#   if temp > 20:
#     return "hot"
#   else:
#     return "cold"
  
def addition(num1, num2):
  return num1 + num2

def divide(num1, num2):
  if num2 == 0:
    raise ValueError("Cannot divide by zero")
  
  return num1 / num2


users = {
  "Zuko" : "zuko@test.gmail",
  "Aang" : "aang@test.gmail"
}
class UserManager():
  def __init__(self):
    self.users = {}

  def add_user(self, username, email):
    if username in self.users:
      raise ValueError("Username already exists")
    self.users[username] = email
    return True
  
  def get_user(self, username):
    if username not in self.users:
      raise ValueError("User does not exist")
    return self.users.get(username)
  
  def set_users(self, users):
    self.users = users
  

avatar_manager = UserManager()
avatar_manager.set_users(users)

class Database():
  def __init__(self):
    self.data = {}

  def add_user(self, id, name):
    if id in self.data:
      raise ValueError("Username already exists")
    self.data[id] = name
    return True
  
  def get_user(self, id):
    return self.data.get(id, None)
  
  def remove_user(self, id):
    if id in self.data:
      del self.data[id]

def is_prime(num):
  if num < 2:
    return False
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      return False
  return True

def get_weather(city):
  response = requests.get(f"https://api.weather.com/v1/{city}")
  if response.status_code == 200:
    return response.json()
  else:
    raise ValueError("Could not fetch")
  
class APIClient:
  """Simulates an extarnal API client."""

  def get_user_data(self, id):
    response = requests.get(f"https://api.example.com/users/{id}")
    if response.status_code == 200:
      return response.json()
    raise ValueError("API request failed")
  
class UserService:
  """Use APIClient to fetch user data and process it."""
  def __init__(self, api_client):
    self.api_client = api_client

  def get_username(self, id):
    user_data = self.api_client.get_user_data(id)
    return user_data["name"].upper()

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {

}

@app.route('/users/<int:user_id>', methods =['GET'])
def get_user(user_id):
  """Returns user info by ID"""

  user = users.get(user_id)
  if user:
    return jsonify({"id": user_id, "name": user}), 200
  return jsonify({"error": "User not found"}), 404

@app.route('/users', methods = ['POST'])
def add_user():
  """Adds user into database"""
  data = request.json 
  user_id = data.get("id")
  name = data.get("name")

  if not user_id or not name:
    return jsonify({"error": "Invalid data"}), 400
  
  if user_id in users:
    return jsonify({"error": "User already exists"}), 402
  
  users[user_id] = name
  return jsonify({"id": user_id, "name": name}), 201

