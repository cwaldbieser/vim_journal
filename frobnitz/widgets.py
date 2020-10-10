

class Widget(object):
    """
    A simulated widget.
    """
    def __init__(self, length, w, h, mass, color):
        self.height = h
        self.length = length
        self.width = w
        self.mass = mass
        self.color = color

    @property
    def volume(self):
        """
        The approximate volume of the widget.
        """
        return self.height * self.width * self.length

    @property
    def density(self):
        """
        The approximate density of the widget.
        """
        return (self.volume / self.mass)

    def __str__(self):
        desc = (
            "A {} widget of size {}x{}x{} units"
            " with volume {} units-cubed and density {}."
        ).format(
            self.color,
            self.length,
            self.width,
            self.height,
            self.volume,
            self.density)
        return desc


class WidgetDimensionsError(Exception):
    pass
