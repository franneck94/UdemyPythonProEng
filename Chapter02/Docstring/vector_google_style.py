# ruff: noqa: ANN204, ANN001, ANN201
"""Own implementation of a 2D vector class.
"""

from __future__ import annotations

import numbers
from functools import total_ordering
from math import sqrt


@total_ordering
class Vector2D:
    """Vector2D class to perform simple vector operations."""

    def __init__(self, x=0, y=0):
        """Create a instance with the given x and y values.

        Args:
            x: x-Value.
            y: y-Value.

        Raises:
            TypeError: If x or y are not a number.
        """
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self.x = x
            self.y = y
        else:
            raise TypeError("You must pass in int/float values for x and y!")

    def __call__(self):
        """Callable for the instance representation.

        Returns:
            The representation of the instance.
        """
        print("Calling the __call__ function!")
        return self.__repr__()

    def __repr__(self):
        """Return the instance representation.

        Returns:
            The representation of the instance.
        """
        return f"vector.Vector2D({self.x}, {self.y})"

    def __str__(self):
        """The instance as a string.

        Returns:
            The instance as a string.
        """
        return f"({self.x}, {self.y})"

    def __bool__(self):
        """Return the truth value of the instance.

        Returns:
            True, if the vector is not the Null-vector.
            False, else.
        """
        return bool(abs(self))

    def __abs__(self):
        """Return the length (magnitude) of the instance.

        Returns:
            Length of the instance.
        """
        return sqrt(self.x**2.0 + self.y**2.0)

    def check_vector_types(self, vector):
        """Check if the vector is an instance of the VectorND class.

        Args:
            vector: A instance.

        Raises:
            TypeError: If vector is not an instance of the VectorND class.
        """
        if not isinstance(self, Vector2D) or not isinstance(vector, Vector2D):
            raise TypeError(
                "You have to pass in two instances of the vector class!"
            )

    def __eq__(self, other_vector):
        """Check if the instances have the same values.

        Args:
            other_vector: Other instance (rhs of the operator)

        Returns:
            True, if the both instances have the same values.
            False, else.
        """
        self.check_vector_types(other_vector)
        is_equal = False
        if self.x == other_vector.x and self.y == other_vector.y:
            is_equal = True
        return is_equal

    def __lt__(self, other_vector):
        """Check if the self instance is less than the other instance.

        Args:
            other_vector: Other instance (rhs of the operator).

        Returns:
            True, if the self instance is less than the other instance.
            False, else.
        """
        self.check_vector_types(other_vector)
        is_less_than = False
        if abs(self) < abs(other_vector):
            is_less_than = True
        return is_less_than

    def __add__(self, other_vector):
        """Returns the addition vector of the self and the other instance.

        Args:
            other_vector: Other instance (rhs of the operator).

        Returns:
            The addition vector of the self and the other instance.
        """
        self.check_vector_types(other_vector)
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector2D(x, y)

    def __sub__(self, other_vector):
        """Return the subtraction vector of the self and the other instance.

        Args:
            other_vector: Other instance (rhs of the operator).

        Returns:
            The subtraction vector of the self and the other instance.
        """
        self.check_vector_types(other_vector)
        x = self.x - other_vector.x
        y = self.y - other_vector.y
        return Vector2D(x, y)

    def __mul__(self, other):
        """Return the multiplication of self and left vector or number.

        Args:
            other: Other instance or scaler value (rhs of the operator)

        Raises:
            TypeError: Not int/float passed in.

        Returns:
            The multiplication of self and left vector or number.
        """
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, numbers.Real):  # noqa: RET505
            return Vector2D(self.x * other, self.y * other)
        else:
            raise TypeError(
                "You must pass in a instance or an int/float number!"
            )

    def __truediv__(self, other):
        """Return the multiplication of self and left vector or number.

        Args:
            other: Other instance or scaler value (rhs of the operator).

        Raises:
            ValueError: Division by zero.
            TypeError: Not int/float passed in.

        Returns:
            The multiplication of self and left vector or number.
        """
        if isinstance(other, numbers.Real):
            if other != 0.0:  # noqa: PLR2004
                return Vector2D(self.x / other, self.y / other)
            else:  # noqa: RET505
                raise ValueError("You cannot divide by zero!")
        else:
            raise TypeError("You must pass in an int/float value!")
