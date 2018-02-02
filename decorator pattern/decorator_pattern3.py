""""
Decorator Pattern - In object-oriented programming, the decorator pattern is a design pattern that allows behaviour to be added to an existing object dynamically. 
The decorator pattern can be used to extend (decorate) the functionality of a certain object at run-time, independently of other instances of the same class, 
provided some groundwork is done at design time.
"""

class foo(object):
    def f1(self):
        print("original f1")
    def f2(self):
        print("original f2")

class foo_decorator(object):
    def __init__(self, decoratee):
        self._decoratee = decoratee
    def f1(self):
        print("decorated f1")
        self._decoratee.f1()
    def __getattr__(self, name):
        return getattr(self._decoratee, name)

u = foo()
v = foo_decorator(u)
v.f1()
v.f2()