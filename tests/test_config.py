from typing import List, Type

import pytest
from _pytest.compat import nullcontext

from src.config import Body, Orbit


@pytest.mark.parametrize(
    argnames=["name", "bodies", "t", "exception"],
    argvalues=[
        (
            "VALID_ORBIT",
            [
                Body(x=0, vx=0, y=0, vy=0, mass=1, name="body_1"),
                Body(x=1, vx=1, y=1, vy=1, mass=1, name="body_2"),
            ],
            10,
            None,
        ),
        ("INVALID_ORBIT", [], 10, ValueError),
        (
            "INVALID_ORBIT",
            [Body(x=0, vx=0, y=0, vy=0, mass=1, name="body_1")],
            10,
            ValueError,
        ),
    ],
)
def test_orbit_constructor(
    name: str, bodies: List[Body], t: int, exception: Type[BaseException]
):
    """ Tests that Orbit constructor raises ValueError if not enough bodies supplied """
    with pytest.raises(exception) if exception else nullcontext():
        Orbit(name=name, bodies=bodies, t=t)
