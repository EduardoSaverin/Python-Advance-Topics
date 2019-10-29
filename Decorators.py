# Method 1 : Classic Way of writing Decorator
def outer_function(fun):
    def wrapper_function():
        print('Wrapper')
        return fun()
    return wrapper_function

def say():
    print('This is message')
    
hi = outer_function(say)

hi()

# Method 2 : Python way

@outer_function
def message():
    print('Say hello')
    
message()


# Passing Arguments : Generic way that will work for all function with or without arguments
def function_decorator(fun):
    def wrapper_function(*args, **kargs):
        print('Generic Wrapper')
        return fun(*args, **kargs)
    return wrapper_function

class class_decorator(object):
    def __init__(self, function_name): 
        self.function_name = function_name
        
    def __call__(self, *args, **kwargs):
        print('Class Decorator')
        self.function_name(*args,**kwargs)
        
@function_decorator
def say_hi(msg):
    print(msg)
    
@class_decorator
def say_bye(msg):
    print(msg)
    
say_hi('Hi')
say_bye('Bye')