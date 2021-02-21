import pytest
from contextlib import nullcontext as DoesNotRaise

from utils.objects import Body, Orbit


@pytest.mark.parametrize(
    argnames=["name", "bodies", "t", "dt", "exception"],
    argvalues=[
        (
            "VALID_ORBIT",
            [
                Body(x=0, vx=0, y=0, vy=0, mass=1, name="body_1"),
                Body(x=1, vx=1, y=1, vy=1, mass=1, name="body_2"),
            ],
            10,
            1000,
            DoesNotRaise(),
        ),
        ("INVALID_ORBIT", [], 10, 1500, pytest.raises(ValueError)),
        (
            "INVALID_ORBIT",
            [Body(x=0, vx=0, y=0, vy=0, mass=1, name="body_1")],
            10,
            10000,
            pytest.raises(ValueError),
        ),
    ],
)
def test_orbit_constructor(name, bodies, t, dt, exception):
    """ Tests that Orbit constructor raises ValueError if not enough bodies supplied """
    with exception:
        Orbit(name=name, bodies=bodies, t=t, dt=dt)
