"""
This file contains the default starting conditions required in order to produce
the plots stored under 'src/plots'.

The starting conditions for:
    - YING_YANG_2B

were taken from: http://three-body.ipb.ac.rs/. Paper: M. Šuvakov and V. Dmitrašinović,
Three Classes of Newtonian Three-Body Planar Periodic Orbits, Phys. Rev. Lett. 110,
114301 (2013). arXiv:1303.0181.
"""
from loaders import Body
from enum import Enum


class DefaultConditions(Enum):
    BROUCKE_A_2 = [
        Body(
            x=0.3361300950,
            y=0.0000000000,
            vx=0.0000000000,
            vy=1.5324315370,
            mass=1,
            name="Body 1",
        ),
        Body(
            x=0.7699893804,
            y=0.0000000000,
            vx=0.0000000000,
            vy=-0.6287350978,
            mass=1,
            name="Body 2",
        ),
        Body(
            x=-1.1061194753,
            y=0.0000000000,
            vx=0.0000000000,
            vy=-0.9036964391,
            mass=1,
            name="Body 3",
        ),
    ]

    BUTTERFLY_IV = [
        Body(x=-1, y=0, vx=0.350112, vy=0.079339, mass=1, name="Body 1"),
        Body(x=1, y=0, vx=0.350112, vy=0.079339, mass=1, name="Body 1"),
        Body(x=0, y=0, vx=-2 * 0.350112, vy=-2 * 0.079339, mass=1, name="Body 1"),
    ]

    TWO_LIGHT_ONE_MASSIVE = [
        Body(x=-50, y=0, vx=0, vy=-10, mass=50, name="Light Body 1"),
        Body(x=0, y=0, vx=0, vy=0, mass=3000, name="Massive Body"),
        Body(x=50, y=0, vx=0, vy=10, mass=50, name="Light Body 2"),
    ]

    YING_YANG_2B = [
        Body(x=-1, y=0, vx=0.417343, vy=0.313100, mass=1, name="Body 1"),
        Body(x=1, y=0, vx=0.417343, vy=0.313100, mass=1, name="Body 1"),
        Body(x=0, y=0, vx=-2 * 0.417343, vy=-2 * 0.313100, mass=1, name="Body 1"),
    ]
