from typing import List

import pytest

from utils.objects import Body
from utils.orbits import calc_2d_distance, calc_dvel, create_initial_conditions


@pytest.mark.parametrize(
    argnames=["bodies", "expected"],
    argvalues=[
        (
            [
                Body(x=0, y=0, vx=0, vy=0, mass=1, name="x"),
                Body(x=1, y=1, vx=1, vy=1, mass=1, name="y"),
            ],
            [0, 0, 0, 0, 1, 1, 1, 1],
        )
    ],
)
def test_create_initial_conditions(bodies: List[Body], expected: List[List[int]]):
    actual = create_initial_conditions(bodies=bodies)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["x1", "y1", "x2", "y2", "expected"],
    argvalues=[(0, 0, 0, 0, 0), (0, 0, 1, 0, 1), (0, 0, 1, 1, 1.4142135623730951)],
)
def test_calc_2d_distance(x1: float, y1: float, x2: float, y2: float, expected: float):
    actual = calc_2d_distance(x1=x1, y1=y1, x2=x2, y2=y2)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["c1", "c2", "r", "m2", "expected"],
    argvalues=[(0, 1, 1, 10, 10.0), (1, 0, 1, 10, -10.0)],
)
def test_calc_dvel(c1: float, c2: float, r: float, m2: float, expected: float):
    actual = calc_dvel(c1=c1, c2=c2, r=r, m2=m2)
    assert actual == expected
