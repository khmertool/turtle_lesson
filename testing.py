# practice to use function in mydraw.py file

from mydraw import DrawStar, DrawSun, DrawSquare

# type command to tell machine the the shaps
command = input("Please, write:\nstar, sun or square? ")

if command == "star":
    DrawStar()
elif command == "sun":
    DrawSun()
elif command == "square":
    DrawSquare()
else:
    print("Do nothing")