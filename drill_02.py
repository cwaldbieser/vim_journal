# Vim Drill:
# Practice commenting and uncommenting the target function in this example
# Python file.  Don't forget to use movements and don't just spam j/k or
# up/down!


def main():
    """
    The program main entry point.
    """
    print("This is an example program.")
    greet("World")


def frotz(magic):
    """
    A magic function that should be commented out for this exercise.
    """
    print("The magic word is: {}".format(magic))


def greet(name):
    """
    Display a simple greeting.
    """
    print("Hello, {}!".format(name))


if __name__ == "__main__":
    main()
