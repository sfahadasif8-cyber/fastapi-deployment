def greet(name):
    return f"Hello, {name}!"
def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
       raise ValueError("Cannot divide by zero.")
    return a / b
def subtract(a, b):
    return a - b    

if __name__ == "__main__":
    print(greet("Fahad"))
    print(add(5, 3))
    print(multiply(5, 3))
    print(divide(10, 2))
    print(subtract(10, 5))