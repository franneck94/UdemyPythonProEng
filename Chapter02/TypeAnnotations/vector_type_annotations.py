"""Own implementation of a 2D vector class.
"""

from __future__ import annotations

from functools import total_ordering
from math import sqrt


@total_ordering
class Vector2D:
    """Vector2D class to perform simple vector operations."""

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        """Create a instance with the given x and y values.

        Args:
            x (float, optional): x-Value. Defaults to 0.
            y (float, optional): y-Value. Defaults to 0.

        Raises:
            TypeError: If x or y are not a number.
        """
        if isinstance(x, float) and isinstance(y, float):
            self.x = x
            self.y = y
        else:
            raise TypeError("You must pass in int/float values for x and y!")

    def __call__(self) -> str:
        """Callable for the instance representation.

        Returns:
            str: The representation of the instance.
        """
        print("Calling the __call__ function!")
        return self.__repr__()

    def __repr__(self) -> str:
        """Return the instance representation.

        Returns:
            str: The representation of the instance.
        """
        return f"vector.Vector2D({self.x}, {self.y})"

    def __str__(self) -> str:
        """The instance as a string.

        Returns:
            str: The instance as a string.
        """
        return f"({self.x}, {self.y})"

    def __bool__(self) -> bool:
        """Return the truth value of the instance.

        Returns:
            bool: True, if the vector is not the Null-vector. False, else.
        """
        return bool(abs(self))

    def __abs__(self) -> float:
        """Return the length (magnitude) of the instance.

        Returns:
            float: Length of the instance.
        """
        return sqrt(self.x**2.0 + self.y**2.0)

    def check_vector_types(self, vector: object) -> None:
        """Check if the vector is an instance of the Vector2D class.

        Args:
            vector (object): A instance.

        Raises:
            TypeError: If vector is not an instance of the Vector2D class.
        """
        if not isinstance(self, Vector2D) or not isinstance(vector, Vector2D):
            raise TypeError(
                "You have to pass in two instances of the vector class!"
            )

    def __eq__(self, other_vector: object) -> bool:
        """Check if the instances have the same values.

        Args:
            other_vector (object): Other instance (rhs of the operator)

        Returns:
            bool: True, if the both instances have the same values. False, else.
        """
        self.check_vector_types(other_vector)
        is_equal = False
        if (
            isinstance(other_vector, Vector2D)
            and self.x == other_vector.x
            and self.y == other_vector.y
        ):
            is_equal = True
        return is_equal

    def __lt__(self, other_vector: Vector2D) -> bool:
        """Check if the self instance is less than the other instance.

        Args:
            other_vector (Vector2D): Other instance (rhs of the operator).

        Returns:
            bool: True, if the self is less than the left instance. False, else.
        """
        self.check_vector_types(other_vector)
        is_less_than = False
        if abs(self) < abs(other_vector):
            is_less_than = True
        return is_less_than

    def __add__(self, other_vector: Vector2D) -> Vector2D:
        """Returns the addition vector of the self and the other instance.

        Args:
            other_vector (Vector2D): Other instance (rhs of the operator).

        Returns:
            Vector2D: The addition vector of the self and the other instance.
        """
        self.check_vector_types(other_vector)
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector2D(x, y)

    def __sub__(self, other_vector: Vector2D) -> Vector2D:
        """Return the subtraction vector of the self and the other instance.

        Args:
            other_vector (Vector2D): Other instance (rhs of the operator).

        Returns:
            Vector2D: The subtraction vector of the self and the other instance.
        """
        self.check_vector_types(other_vector)
        x = self.x - other_vector.x
        y = self.y - other_vector.y
        return Vector2D(x, y)

    def __mul__(self, other: Vector2D | float) -> Vector2D | float:
        """Return the multiplication of self and left vector or number.

        Args:
            other (Union[float, Vector2D]): Other instance or scaler
                value (rhs of the operator)

        Raises:
            TypeError: Not int/float passed in.

        Returns:
            Union[float, Vector2D]: The multiplication of self and the
            other vector(or number) instance.
        """
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, float):  # noqa: RET505
            return Vector2D(self.x * other, self.y * other)
        else:
            raise TypeError(
                "You must pass in a instance or an int/float number!"
            )

    def __truediv__(self, other: float) -> Vector2D:
        """Return the multiplication of self and left vector or number.

        Args:
            other: Other instance or scaler value (rhs of the operator).

        Raises:
            ValueError: Division by zero.
            TypeError: Not int/float passed in.

        Returns:
            float: The multiplication of self and left vector or number.
        """
        if isinstance(other, float):
            if other != 0.0:  # noqa: PLR2004
                return Vector2D(self.x / other, self.y / other)
            else:  # noqa: RET505
                raise ValueError("You cannot divide by zero!")
        else:
            raise TypeError("You must pass in an int/float value!")
