from typing import List, NamedTuple


class Body(NamedTuple):
    """ Used to capture the initial configuration for a body in an orbit """

    x: float
    y: float
    vx: float
    vy: float
    mass: float
    name: str


class Orbit:
    """ Class used to store necessary information for n body orbit configurations. """

    def __init__(self, name: str, bodies: List[Body], t: int, dt: int):
        self.name = name
        self.t = t
        self.dt = dt

        if len(bodies) < 2:
            raise ValueError(
                f"Orbit configuration requires at least 2 bodies, "
                f"{len(bodies)} supplied"
            )
        else:
            self.bodies = bodies
