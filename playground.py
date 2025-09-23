users = {
  "Zuko" : "zuko@test.gmail",
  "Aang" : "aang@test.gmail"
}

class UserManager():
  def __init__(self):
    self.users = {}

  def add_user(self, username, email):
    if username in self.users:
      raise ValueError("User already exits")
    self.users[username] = email
    return True

  def get_user(self, username):
    #return self.users.get(username) THIS ALSO WORKS
    return self.users[username]
  
  def get_users(self):
    for username, email in self.users.items():
      print(f"{username} : {email}")

  
#avatar_manager = UserManager(users)

# print("Add user:")
# added_katara = avatar_manager.add_user("Katara", "katara@test.gmail")

# if added_katara:
#   print("Katara have been added successfully!")

# try:
#   avatar_manager.add_user("Zuko", "zuko@test.gmail")
#   print("Zuko have been added successfully")
# except ValueError as error:
#   print(f"Error adding user: {error}")

# print(f"Username: Zuko Email: {avatar_manager.get_user("Zuko")}")

# print("Users :")
# avatar_manager.get_users()
#print(avatar_manager.users.items())

print(int( (8 ** 0.5) + 1))