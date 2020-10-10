
# Vim Drill:
# Practice code navigation:
# - Go to assignments
# - Go to definitions
# - Show docs
# - Rename functions / variables
# - Show usage of name.
# - Remember to use jump list (CTRL-O) to jump back!

from frobnitz.widgets import Widget, WidgetDimensionsError
from frobnitz.box import Box


def main():
    """
    The program main entry point.
    """
    print("This is an example program.")
    widget_a = Widget(10, 15, 22, 2.5, "green")
    print("Created widget A: {}".format(widget_a))
    widget_b = Widget(5, 7.5, 25, 3, "blue")
    print("Created widget B: {}".format(widget_b))
    box01 = Box(9, 9, 30)
    print("Created box {}".format(box01))
    print("Packing widget A into box ...")
    try:
        box01.pack(widget_a)
    except WidgetDimensionsError:
        print("Oops!  The widget won't fit!")
    print("Packing widget B into box ...")
    box01.pack(widget_b)
    print(box01)


if __name__ == "__main__":
    main()
