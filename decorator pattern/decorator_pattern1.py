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

#where you know the class being decorated in advance.
class foo_decorator(foo):
    def __init__(self, decoratee):
        self.__dict__.update(decoratee.__dict__) 
    
    def f1(self):
        print("decorated f1")
        super(foo_decorator, self).f1()
        
        
        
u = foo()
v = foo_decorator(u)
v.f1()
v.f2()
print('isinstance(v, foo) ==', isinstance(v, foo))
        
  