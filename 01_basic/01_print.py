### Printing in Python
print("Hello World!")
print(1 < 2)
print(type(1))
print("Another separation", "type", sep = "-")
print("This is a string", end = "!\n")

### Casting types to another - converting one type to another
print(int(1.5))  # Converts float to int
print(int("123"))  # Converts string to int

print(round(1.5))  # Rounds the float to the nearest integer
print(round(3.6))

print(round(3.14159, 2))  # Rounds the float to 2 decimal places

### Variable assignment
x = 10
my_name = "Zuko"
print(my_name)

### Dynamic typing
x = 10  # x is an integer
x = "Zuko"  # Now x is a string
print(type(x))

### Strong typing Python does not allow implicit type conversion
#print(int("100" + 1)) # This will raise an error because you cannot concatenate string and int directly
#print(int("Hello World"))  # This will raise an error because "Hello World" cannot be converted to int

### f-strings for formatted output
print(f"Hello my name is {my_name}")

### NOT RECOMMENDED VARIABLE ASSIGNMENT
name, age, city = "Zuko", 16, "Ba Sing Se"