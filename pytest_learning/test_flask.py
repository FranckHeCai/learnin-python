from main import app
import pytest

@pytest.fixture
def client():
  """Provides a test client for the Flask app"""
  app.config["TESTING"] == True
  with app.test_client() as client:
    yield client

def test_add_user(client):
  """Test adding a new user."""
  response = client.post('/users', json = {"id": 1, "name": "Alice"})
  assert response.status_code == 201
  assert response.json == {"id": 1, "name": "Alice"}

def test_get_user(client):
  client.post('/users', json = {"id": 1, "name": "Alice"})
  response = client.get('users/1')
  
  assert response.status_code == 200
  assert response.json == {"id": 1, "name": "Alice"}

def test_get_user_not_found(client):
  response = client.get('users/99')

  assert response.status_code == 404
  assert response.json == {"error": "User not found"}

def test_add_duplicate_user(client):
  """Test adding a new user."""
  client.post('/users', json = {"id": 1, "name": "Zuko"})

  response = client.post('/users', json = {"id" : 1, "name": "Alice"})
  assert response.status_code == 402
  assert response.json == {"error": "User already exists"}