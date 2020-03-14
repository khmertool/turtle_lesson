# practice to use function in mydraw.py file

from mydraw import DrawStar, DrawSun, Pandas

# type command to tell machine the the shaps
command = input("Please, write:\nstar, sun or pandas? ")

if command == "star":
    DrawStar()
elif command == "sun":
    DrawSun()
elif command == "pandas":
    Pandas()
else:
    print("Do nothing")