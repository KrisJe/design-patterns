"""
Testing Python decorators against Decorator Pattern
###################################################

Decorators in Python - Despite the name, Python decorators are not an implementation of the decorator pattern. The decorator pattern is 
a design pattern used in statically typed object-oriented programming languages to allow functionality to be added to objects at run time; 
Python decorators add functionality to functions and methods at definition time, and thus are a higher-level construct than decorator-pattern 
classes. The decorator pattern itself is trivially implementable in Python, because the language is duck typed, and so is not usually 
considered as such. So in Python a decorator is any callable Python object that is used to modify a function, method or class definition.
"""

def function(string):
    return string

def decorator(wrapped):
    def wrap(string):
        # assume that this is something useful
        return wrapped(string.upper())
    return wrap

def method_decorator(wrapped):
    def wrap(instance, string):
        # assume that this is something useful
        return wrapped(instance, string.upper())
    return wrap

@decorator
def decorated_function(string):
    print('! '.join(string.split(' ')))

class Class(object):
    def __init__(self):
        pass
    def something_useful(self, string):
        return string

class Decorator(object):
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def something_useful(self, string):
        string = '! '.join(string.split(' '))
        return self.wrapped().something_useful(string)

    @method_decorator
    def decorated_and_useful(self,string):
        return self.something_useful(string)


if __name__ == '__main__':
    string = 'Lorem ipsum dolor sit amet.'
    print(function(string))                  # plain functioon
    print(decorator(function)(string))       # Python decorator at run time
    print(decorated_function(string))        # Python decorator at definition time
    a = Class()
    print(a.something_useful(string))        # plain method
    b = Decorator(Class)
    print(b.something_useful(string))        # Decorator Pattern
    print(b.decorated_and_useful(string))    # Python decorator decorated Decorator Pattern