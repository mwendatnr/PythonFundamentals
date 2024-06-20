
number = 78 # Int
x = 67.32 # Float
greeting = "Hello there" # String
isPythonInteresting = True # Bool
devices = ["laptop", "computer", "tablet"] # List
browsers = ("opera","firefox", "chrome", "safari") # Tuple
countries = {"Kenya","Sudan","Rwanda"} # Set
student = {
    "firstname": "Tevin",
    "age": 18,
    "course": "MIT"
} # Dictionary

print(countries)
print(isPythonInteresting)
print(x)
print(devices)
print(student["firstname"])
print(student["age"])


# Determining the datatype

print(type(devices))
print(type(student))

# Typecasting is the process of converting one data type to another
print(int(x))
print(float(number))