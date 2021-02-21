"""
This file contains the default starting conditions required in order to produce
the plots stored under 'src/plots'.

The starting conditions for:
    - BROUCKE_A_2
    - BUTTERFLY_IV
    - DRAGONFLY_II_15_A
    - YING_YANG_2B

were taken from: http://three-body.ipb.ac.rs/. Paper: M. Šuvakov and V. Dmitrašinović,
Three Classes of Newtonian Three-Body Planar Periodic Orbits, Phys. Rev. Lett. 110,
114301 (2013). arXiv:1303.0181.
"""

from utils.objects import Body, Orbit

# TODO: these could be in an Enum
BROUCKE_A_2 = Orbit(
    name="BROUCKE_A_2",
    bodies=[
        Body(x=0.3361300950, y=0.0, vx=0.0, vy=1.5324315370, mass=1, name="Body 1",),
        Body(x=0.7699893804, y=0.0, vx=0.0, vy=-0.6287350978, mass=1, name="Body 2",),
        Body(x=-1.1061194753, y=0.0, vx=0.0, vy=-0.9036964391, mass=1, name="Body 3",),
    ],
    t=8,
    dt=1000,
)

BUTTERFLY_IV = Orbit(
    name="BUTTERFLY_IV",
    bodies=[
        Body(x=-1, y=0, vx=0.350112, vy=0.079339, mass=1, name="Body 1"),
        Body(x=1, y=0, vx=0.350112, vy=0.079339, mass=1, name="Body 1"),
        Body(x=0, y=0, vx=-2 * 0.350112, vy=-2 * 0.079339, mass=1, name="Body 1"),
    ],
    t=80,
    dt=10000,
)

DRAGONFLY_II_15_A = Orbit(
    name="DRAGONFLY_II_15_A",
    bodies=[
        Body(x=-1, y=0, vx=0.049051, vy=0.590194, mass=1, name="Body 1"),
        Body(x=1, y=0, vx=0.049051, vy=0.590194, mass=1, name="Body 1"),
        Body(x=0, y=0, vx=-2 * 0.049051, vy=-2 * 0.590194, mass=1, name="Body 1"),
    ],
    t=60,
    dt=5000,
)

TWO_LIGHT_ONE_MASSIVE = Orbit(
    name="TWO_LIGHT_ONE_MASSIVE",
    bodies=[
        Body(x=-50, y=0, vx=0, vy=-10, mass=50, name="Light Body 1"),
        Body(x=0, y=0, vx=0, vy=0, mass=3000, name="Massive Body"),
        Body(x=50, y=0, vx=0, vy=10, mass=50, name="Light Body 2"),
    ],
    t=204,
    dt=1000,
)

YING_YANG_2B = Orbit(
    name="YING_YANG_2B",
    bodies=[
        Body(x=-1, y=0, vx=0.417343, vy=0.313100, mass=1, name="Body 1"),
        Body(x=1, y=0, vx=0.417343, vy=0.313100, mass=1, name="Body 1"),
        Body(x=0, y=0, vx=-2 * 0.417343, vy=-2 * 0.313100, mass=1, name="Body 1"),
    ],
    t=55,
    dt=10000,
)

DEFAULT_ORBITS = {
    o.name: o
    for o in [
        BROUCKE_A_2,
        BUTTERFLY_IV,
        DRAGONFLY_II_15_A,
        TWO_LIGHT_ONE_MASSIVE,
        YING_YANG_2B,
    ]
}
