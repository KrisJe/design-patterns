""""
Decorator Pattern - In object-oriented programming, the decorator pattern is a design pattern that allows behaviour to be added to an existing object dynamically. 
The decorator pattern can be used to extend (decorate) the functionality of a certain object at run-time, independently of other instances of the same class, 
provided some groundwork is done at design time.
""" 

#you don't need to know the class you're decorating in advance        
class Decorator(object):
    def __new__(cls, decoratee):
        cls = type('decorated',
                   (cls, decoratee.__class__),
                   decoratee.__dict__)
        return object.__new__(cls)



class SpecificDecorator(Decorator):
    def f1(self):
        print("decorated f1")
        super(SpecificDecorator, self).f1()
        

class Decorated(object):
    def f1(self):
        print("original f1")



d = SpecificDecorator(Decorated())
d.f1()
