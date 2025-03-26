# Importing modules (import, from, as)
import math  # import
from datetime import datetime as dt  # from, as

class ExampleClass:
    # Using class and demonstrating methods
    def __init__(self, value=None):  # None as default value
        self.value = value
    
    def show_value(self):
        return self.value

def greet(name=None):  # Function updated to use None
    # Function to demonstrate def, return, if, else, None
    if name is not None:  # is, None
        return f"Hello, {name}!"  # return
    else:  # else
        return "Hello, Stranger!"

def calculate_square_root(number):
    # Function to demonstrate assert, global
    global last_result  # global
    assert number >= 0, "Number must be positive!"  # assert
    last_result = math.sqrt(number)
    return last_result  # return

def loop_example():
    # Demonstrating for, while, break, continue, and pass
    for i in range(5):  # for, in
        if i == 3:
            break  # break
        elif i == 1:
            continue  # continue
        print("Loop iteration:", i)
    
    i = 0
    while i < 3:  # while
        i += 1
        pass  # pass

def boolean_demo():
    # Using and, or, not, True, False
    x, y = True, False  # True, False
    if x and not y:  # and, not
        print("Condition met")
    elif x or y:  # or, elif
        print("One condition is true")
    else:
        print("No conditions met")

def error_handling():
    # Using try, except, raise, finally
    try:
        raise ValueError("Oops! An error occurred")  # raise
    except ValueError as e:  # except, as
        print("Error caught:", e)
    finally:  # finally
        print("This will always run.")

def use_lambda():
    # Using lambda function
    square = lambda x: x * x  # lambda
    print("Square of 4:", square(4))

def generate_numbers():
    # Using yield in a generator function
    def number_generator():
        yield 1  # yield
        yield 2
    
    gen = number_generator()
    print(next(gen))
    print(next(gen))

def modify_variable():
    # Using nonlocal keyword
    text = "old"
    
    def inner():
        nonlocal text  # nonlocal
        text = "new"
    
    inner()
    print("Modified variable:", text)

def file_example():
    # Using with to handle a file
    with open("example.txt", "w") as file:  # with, as
        file.write("Learning Python keywords!")

# Running functions
example = ExampleClass("Example Value")  # Using class
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
