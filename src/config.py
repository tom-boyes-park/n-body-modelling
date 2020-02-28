from typing import List

from loaders import Body
from enum import Enum, auto


class DefaultBodies(Enum):
    TWO_LIGHT_ONE_MASSIVE = auto()
    YING_YANG_2B = auto()


DEFAULT_POSITIONS = {
    DefaultBodies.TWO_LIGHT_ONE_MASSIVE: [
        Body(x=-50, y=0, vx=0, vy=-10, mass=50, name="Light Body 1"),
        Body(x=0, y=0, vx=0, vy=0, mass=3000, name="Massive Body"),
        Body(x=50, y=0, vx=0, vy=10, mass=50, name="Light Body 2"),
    ],
    DefaultBodies.YING_YANG_2B: [
        Body(x=-1, y=0, vx=0.417343, vy=0.313100, mass=1, name="Body 1"),
        Body(x=1, y=0, vx=0.417343, vy=0.313100, mass=1, name="Body 1"),
        Body(x=0, y=0, vx=-2 * 0.417343, vy=-2 * 0.313100, mass=1, name="Body 1"),
    ],
}


def get_default_bodies(default_bodies: DefaultBodies) -> List[Body]:
    return DEFAULT_POSITIONS.get(default_bodies)
