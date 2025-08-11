### Input function to get user input
#print("Please enter your name:")
user_name = input("Please enter your name: ")  # Waits for user input and assigns it to user_name
print(f"Hello {user_name}!")

age = input("Please enter your age: ")  # Gets age as a string
print(f"In 20 years you will be {int(age) + 20} years old!")  # Converts age to int and adds 20

country, city = input("Please enter your country and city: ").split()
print(f"You are from {city}, {country}!")  # Prints the city and country
