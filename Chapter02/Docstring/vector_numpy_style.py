# ruff: noqa: ANN204, ANN001, ANN201
from functools import total_ordering
from math import sqrt


@total_ordering
class Vector2D:
    def __init__(self, x=0.0, y=0.0):
        """Create a vector2d object.

        Parameters
        ----------
        x : float, optional
            The x-coordinate of the 2d vector, by default 0.0
        y : float, optional
            The y-coordinate of the 2d vector, by default 0.0

        Raises
        ------
        TypeError
            You must pass in int/float values for x and y!
        """
        if isinstance(x, float) and isinstance(y, float):
            self.x = x
            self.y = y
        else:
            raise TypeError("You must pass in int/float values for x and y!")

    def __call__(self):
        print("Calling the __call__ function!")
        return self.__repr__()

    def __repr__(self):
        return f"vector.Vector2D({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __bool__(self):
        return bool(abs(self))

    def __abs__(self):
        """This is a summary

        Returns
        -------
        dtype
            This is a description of the return value.
        """
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def check_vector_types(self, vector2):
        if not isinstance(self, Vector2D) or not isinstance(vector2, Vector2D):
            raise TypeError(
                "You have to pass in two instances of the vector class!"
            )

    def __eq__(self, other_vector):
        self.check_vector_types(other_vector)
        if self.x == other_vector.x and self.y == other_vector.y:
            return True
        return False

    def __lt__(self, other_vector):
        self.check_vector_types(other_vector)
        if abs(self) < abs(other_vector):
            return True
        return False

    def __add__(self, other_vector):
        self.check_vector_types(other_vector)
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector2D(x, y)

    def __sub__(self, other_vector):
        try:
            x = self.x - other_vector.x
            y = self.y - other_vector.y
            return Vector2D(x, y)
        except AttributeError as e:
            print(f"AttributeError: {e} was raised!")
            return self

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        if isinstance(other, float):
            return Vector2D(self.x * other, self.y * other)
        raise TypeError("You must pass in a instance or an int/float number!")

    def __truediv__(self, other):
        if isinstance(other, float):
            if other != 0.0:  # noqa: PLR2004
                return Vector2D(self.x / other, self.y / other)
            raise ValueError("You cannot divide by zero!")
        raise TypeError("You must pass in an int/float value!")
