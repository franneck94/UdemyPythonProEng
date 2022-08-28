from typing import Any

import pytest
from fastvector import Vector2D


V1 = Vector2D(0, 0)
V2 = Vector2D(-1, 1)
V3 = Vector2D(2.5, -2.5)


@pytest.mark.parametrize(
    ('lhs', 'rhs', 'exp_res'),
    (
        (V1, V2, Vector2D(-1, 1)),
        (V1, V3, Vector2D(2.5, -2.5)),
        (V3, V2, Vector2D(1.5, -1.5)),
        (V3, V1, Vector2D(2.5, -2.5))
    )
)
def test_add(lhs: Vector2D, rhs: Vector2D, exp_res: Vector2D) -> None:
    assert lhs + rhs == exp_res


@pytest.mark.parametrize(
    ('lhs', 'rhs', 'exp_res'),
    (
        (V1, V2, Vector2D(1, -1)),
        (V1, V3, Vector2D(-2.5, 2.5)),
        (V3, V2, Vector2D(3.5, -3.5)),
    )
)
def test_sub(lhs: Vector2D, rhs: Vector2D, exp_res: Vector2D) -> None:
    assert lhs - rhs == exp_res


@pytest.mark.parametrize(
    ('lhs', 'rhs', 'exp_res'),
    (
        (V1, V2, 0.0),
        (V1, V3, 0.0),
        (V3, V2, -5.0),
    )
)
def test_mul_vec(lhs: Vector2D, rhs: Vector2D, exp_res: float) -> None:
    assert lhs * rhs == exp_res


@pytest.mark.parametrize(
    ('lhs', 'rhs', 'exp_res'),
    (
        (V1, 2.0, Vector2D(0.0, 0.0)),
        (V2, 2.0, Vector2D(-2.0, 2.0)),
        (V3, 2.0, Vector2D(5.0, -5.0)),
    )
)
def test_mul_float(lhs: Vector2D, rhs: float, exp_res: Vector2D) -> None:
    assert lhs * rhs == exp_res


@pytest.mark.skip(reason="Not implemented")
def test_abs() -> None:
    pass


@pytest.mark.parametrize(
    ('x', 'y'),
    (
        (-1, None),
        (None, -1),
        (None, None),
    )
)
def test_raises(x: Any, y: Any) -> None:
    with pytest.raises(TypeError):
        _ = Vector2D(x, y)
