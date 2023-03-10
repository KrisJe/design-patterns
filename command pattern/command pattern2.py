from abc import ABCMeta
from abc import abstractmethod
import inspect
import os

class Command(object):
    """
    Abstract / Interface base class for commands.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class CreateCommand(Command):
    """
    Create command implementation.
    """
    def __init__(self, name):
        self.file_name = name

    def execute(self, name):
        open(self.file_name, 'w')
        print str(self) + ':::Method:::' + inspect.stack()[0][3]

    def undo(self):
        os.remove(self.file_name)
        print str(self) + ':::Method:::' + inspect.stack()[0][3]


class MoveCommand(Command):
    """
    Move command implementation.
    """
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self, src, dest):
        os.rename(self.src, self.dest)
        print str(self) + ':::Method:::' + inspect.stack()[0][3]

    def undo(self):
        os.rename(self.dest, self.src)
        print str(self) + ':::Method:::' + inspect.stack()[0][3]


class Invoker(object):

    def __init__(self, command):
        self.command = command

    def do(self):
        self.command.execute()

    def undo(self):
        self.command.undo() 


# Client for the command pattern
if __name__ == '__main__':
    create_cmd = CreateCommand('/tmp/foo.txt')
    move_cmd = MoveCommand('/tmp/foo.txt', '/tmp/bar.txt')
    create_invoker = Invoker(create_cmd)
    move_invoker = Invoker(move_cmd)
    create_invoker.do()
    move_invoker.do()
    move_invoker.undo()
    create_invoker.undo()