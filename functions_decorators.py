"""Examples of weird function things and decorators"""


# functions as inputs
def say_hello(name):
    return f"Hello {name}"


def be_cool(name):
    return f"Yo {name}, together we are cool! "


def greet_bob(greeter_func):
    return greeter_func("Bob")


# functions inside functions
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")


# Decorators
def my_decorator(func):
    def wrapper(text_value):
        print("Something is happening before the function is called")
        func(text_value)
        print("Something is happening after the function is called")

    return wrapper


def say_whee():
    print("Wheee!")


# What a decorator does
say_whee = my_decorator(say_whee)


# Decorator syntax
@my_decorator
def say_whee_2(text_value):
    print(text_value)


say_whee_2("Whee!")
