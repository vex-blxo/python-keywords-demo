import math  
from datetime import datetime as dt  

class ExampleClass:
    def __init__(self, value=None): 
        self.value = value
    
    def show_value(self):
        return self.value

def greet(name=None): 
    
    if name is not None: 
        return f"Hello, {name}!"  
    else:  
        return "Hello, Stranger!"

def calculate_square_root(number):
    global last_result  
    assert number >= 0, "Number must be positive!" 
    last_result = math.sqrt(number)
    return last_result  

def loop_example():
    for i in range(5): 
        if i == 3:
            break
        elif i == 1:
            continue
        print("Loop iteration:", i)
    
    i = 0
    while i < 3:
        i += 1
        pass 

def boolean_demo():
    x, y = True, False  
    if x and not y: 
        print("Condition met")
    elif x or y: 
        print("One condition is true")
    else:
        print("No conditions met")

def error_handling():
    try:
        raise ValueError("Oops! An error occurred") 
    except ValueError as e: 
        print("Error caught:", e)
    finally: 
        print("This will always run.")

def use_lambda():
    square = lambda x: x * x  
    print("Square of 4:", square(4))

def generate_numbers():
    def number_generator():
        yield 1  # yield
        yield 2
    
    gen = number_generator()
    print(next(gen))
    print(next(gen))

def modify_variable():
    text = "old"
    
    def inner():
        nonlocal text  
        text = "new"
    
    inner()
    print("Modified variable:", text)

def file_example():
    with open("example.txt", "w") as file:
        file.write("Learning Python keywords!")

example = ExampleClass("Example Value") 
print("Class value:", example.show_value())

print(greet("Alice"))
loop_example()
boolean_demo()
error_handling()
use_lambda()
generate_numbers()
modify_variable()
file_example()
print("Square root of 25:", calculate_square_root(25))
