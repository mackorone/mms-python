import sys

class MouseCrashedError(Exception):
    pass

def command(args, return_type=None):
    line = " ".join([str(x) for x in args]) + "\n"
    sys.stdout.write(line)
    sys.stdout.flush()
    if return_type:
        response = sys.stdin.readline().strip()
        if return_type == bool:
            return response == "true"
        return return_type(response)

def mazeWidth():
    return command(args=["mazeWidth"], return_type=int)

def mazeHeight():
    return command(args=["mazeHeight"], return_type=int)

def wallFront():
    return command(args=["wallFront"], return_type=bool)

def wallRight():
    return command(args=["wallRight"], return_type=bool)

def wallLeft():
    return command(args=["wallLeft"], return_type=bool)

def moveForward():
    response = command(args=["moveForward"], return_type=str)
    if response == "crash":
        raise MouseCrashedError()

def turnRight():
    command(args=["turnRight"], return_type=str)

def turnLeft():
    command(args=["turnLeft"], return_type=str)

def setWall(x, y, direction):
    command(args=["setWall", x, y, direction])

def clearWall(x, y, direction):
    command(args=["clearWall", x, y, direction])

def setColor(x, y, color):
    command(args=["setColor", x, y, color])

def clearColor(x, y):
    command(args=["clearColor", x, y])

def clearAllColor():
    command(args=["clearAllColor"])

def setText(x, y, text):
    command(args=["setText", x, y, text])

def clearText(x, y):
    command(args=["clearText", x, y])

def clearAllText():
    command(args=["clearAllText"])

def wasReset():
    return command(args=["wasReset"], return_type=bool)

def ackReset():
    command(args=["ackReset"], return_type=str)
