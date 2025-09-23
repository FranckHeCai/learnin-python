from main import get_weather, addition, divide, UserManager, avatar_manager, Database, is_prime, APIClient, UserService
import pytest

# def test_get_weather():
#   assert get_weather(21) == "hot"
#   assert get_weather(12) == "cold"

def test_addition():
  assert addition(3, 5) == 8

def test_divide():
  assert divide(6,3) == 2
  with pytest.raises(ValueError, match="Cannot divide by zero"):
    divide(10, 0)

@pytest.fixture
def user_manager():
  """Creates a new UserManager class before each test"""
  return UserManager()

@pytest.fixture
def avatar_manager_fixture():
  return avatar_manager

@pytest.fixture
def db():
  database = Database()
  yield database
  database.data.clear()

def test_add_user(user_manager):
  assert user_manager.add_user("Zuko", "zuko@test.gmail") == True
  assert user_manager.get_user("Zuko") == "zuko@test.gmail"

def test_add_duplicate_user(avatar_manager_fixture):
  with pytest.raises(ValueError, match= "User does not exist"):
    assert avatar_manager_fixture.get_user("Katara")
  with pytest.raises(ValueError, match="Username already exists"):
    avatar_manager_fixture.add_user("Zuko", "anything")

def test_add_duplicate_user_global():
  with pytest.raises(ValueError, match= "User does not exist"):
    assert avatar_manager.get_user("Katara")
  with pytest.raises(ValueError, match="Username already exists"):
    avatar_manager.add_user("Zuko", "anything")

def test_db_add_user(db):
  assert db.add_user("1", "Zuko") == True
  assert db.get_user("1")

def test_db_duplicate_user(db):
  db.add_user("1", "Zuko")
  with pytest.raises(ValueError, match="Username already exists"):
    assert db.add_user("1", "Zuko")

def test_db_delete_user(db):
  db.add_user(1, "Zuko")
  db.remove_user(1)
  assert db.get_user(1) is None

@pytest.mark.parametrize('num, expected', [
  (1, False),
  (2, True),
  (3, True),
  (4, False),
  (17, True),
  (19, True),
  (25, False),
])

def test_is_prime(num, expected):
  assert is_prime(num) == expected

def test_get_weather(mocker):
  mock_get = mocker.patch("main.requests.get")

  mock_get.return_value.status_code = 200
  mock_get.return_value.json.return_value = {"temperature": 25, "condition": "Sunny"}

  result = get_weather("Dubai")

  assert result == {"temperature": 25, "condition": "Sunny"}
  mock_get.assert_called_once_with("https://api.weather.com/v1/Dubai")

def test_api_get_username(mocker):
  mock_api_client = mocker.Mock(spec = APIClient)

  mock_api_client.get_user_data.return_value = {"id": 1, "name": "Alice"}

  service = UserService(mock_api_client)
  result = service.get_username(1)

  assert result == "ALICE"
  mock_api_client.get_user_data.assert_called_once_with(1)