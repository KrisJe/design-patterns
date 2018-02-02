""" C#-like events in Python """

# glue code
class event(object):
    def __init__(self, func):
        self.__doc__ = func.__doc__
        self._key = ' ' + func.__name__      
    def __get__(self, obj, cls):        
        try:          
            return obj.__dict__[self._key]        
        except KeyError:
            be = obj.__dict__[self._key] = boundevent()           
            return be

class boundevent(object):
    def __init__(self):
        self._fns = []
        print("init")
    def __iadd__(self, fn):
        print("append")
        self._fns.append(fn)
        return self
    def __isub__(self, fn):
        self._fns.remove(fn)
        return self
    def __call__(self, *args, **kwargs):
        for f in self._fns[:]:
            #print(len(self._fns))
            f(*args, **kwargs)
           

# producer
class MyJob(object):           
        
    @event
    def progress(pct):
        """Called when progress is made. pct is the percent complete."""   
     

    def run(self):
        n = 10
        for i in range(n+1):
            self.progress(100.0 * i / n)
            
   
     
class progressBar(object):    
    _cal_factor = 0.0    
    def __init__(self):
        self._cal_factor = 1.689
    def update(self,pct):
        print("%.1f%% observer C\n" % (pct*self._cal_factor))

#consumer
import sys
job = MyJob()
a = progressBar()
job.progress += lambda pct: sys.stdout.write("%.1f%% observer A\n" % pct)
job.progress += lambda pct: sys.stdout.write("%.1f%% observer B\n" % (pct*1.2))
job.progress += lambda pct: a.update(pct)
# This works exactly like the "simple observer" code above, but you can add as many listeners as you like using +=.
# job.progress += ...
job.run()