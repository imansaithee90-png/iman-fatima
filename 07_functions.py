# Program 7: Functions and Scope

# Function without parameters
def greet():
    print("Hello! Welcome to Python.")

greet()


# Function with parameters
def add(a, b):
    print("Sum:", a + b)

add(10, 5)


# Function with return value
def multiply(a, b):
    return a * b

result = multiply(4, 3)
print("Multiplication:", result)


# Local Variable
def show_local():
    x = 10
    print("Local variable:", x)

show_local()


# Global Variable
x = 100

def show_global():
    print("Global variable:", x)

show_global()
print("Outside function:", x)