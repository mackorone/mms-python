import API
import sys

def log(string):
    sys.stderr.write("{}\n".format(string))

def main():
    while True:
        if not API.wallLeft():
            log("turnLeft")
            API.turnLeft()
        while API.wallFront():
            log("turnRight")
            API.turnRight()
        log("moveForward")
        API.moveForward()

if __name__ == "__main__":
    main()
