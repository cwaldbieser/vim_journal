

class Box(object):
    """
    A simulated box.
    """
    def __init__(self, length, w, h):
        self.length = length
        self.width = w
        self.height = h
        self.widgets = []

    @property
    def volume(self):
        """
        The volume of the box.
        """
        return self.height * self.width * self.length

    def pack(self, widget):
        """
        Pack a widget in the box.
        """
        if self.width < widget.width:
            raise WidgetDimensionsError("The widget is too wide to pack.")
        if self.height < widget.height:
            raise WidgetDimensionsError("The widget is too tall to pack.")
        if self.length < widget.length:
            raise WidgetDimensionsError("The widget is too long to pack.")
        self.widgets.append(widget)

    def __str__(self):
        desc = "A box of dimensions {}x{}x{} units".format(
            self.length,
            self.width,
            self.height)
        parts = [desc]
        if len(self.widgets) > 0:
            parts.append("Inside is packed:")
            for widget in self.widgets:
                parts.append("- {}".format(widget))
        return "\n".join(parts)

