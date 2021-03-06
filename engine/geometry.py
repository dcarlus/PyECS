class Point():
    """Define a 2D point."""

    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.m_x = x
        self.m_y = y

    @property
    def x(self) -> int:
        """Get the X coordinate of the Point."""
        return self.m_x

    @property
    def y(self) -> int:
        """Get the Y coordinate of the Point."""
        return self.m_y

    @x.setter
    def x(self, x: int) -> None:
        """Get the X coordinate of the Point."""
        self.m_x = x

    @y.setter
    def y(self, y: int) -> None:
        """Get the Y coordinate of the Point."""
        self.m_y = y

    def __str__(self):
        """Return a string for representing the Point."""
        return '({}, {})'.format(self.m_x, self.m_y)

    def asSequence(self) -> (int, int):
        """Return the Point as a sequence of numbers (x, y)."""
        return self.m_x, self.m_y

    def asTuple(self) -> [int, int]:
        """Return the Point as a tuple of numbers [x, y]."""
        return [self.m_x, self.m_y]

    def multiplied(self, factor: int) -> 'Point':
        """Create a new Point in which the coordinates of the current Point are mutiplied by a given factor."""
        return Point(self.x * factor, self.y * factor)

    def __add__(self, other: 'Point') -> 'Point':
        """Define the operator + on Point."""
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point') -> 'Point':
        """Define the operator - on Point."""
        return Point(self.x - other.x, self.y - other.y)
