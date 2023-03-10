


class Command(object):
    def execute(self, canvas):
         raise NotImplementedError

# command
class DrawLineCommand(Command):
    def __init__(self, point1, point2):
        self._point1 = point1
        self._point2 = point2

    def execute(self, canvas):
        canvas.draw_line(self._point1, self._point2)

# command
class DrawCircleCommand(Command):
     def __init__(self, point, radius):
        self._point = point
        self._radius = radius

     def execute(self, canvas):
        canvas.draw_circle(self._point, self._radius)

# invoker
class UndoHistory(object):
    def __init__(self, canvas):
        self._commands = []
        self.canvas = canvas

    def command(self, command):
        self._commands.append(command)
        command.execute(self.canvas)

    def undo(self):
        self._commands.pop() # throw away last command
        self.canvas.clear()
        for command in self._commands:
            command.execute(self.canvas)
            
            

create_cmd = Command()

drawline = DrawLineCommand(1, 2)

myinvoker = UndoHistory(drawline)


myinvoker.command(drawline)