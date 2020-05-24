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
from typing import List


class Body:
    def __init__(self, x, vx, y, vy, mass, name):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.name = name


class Orbit:
    """ Class used to store necessary information for n body orbit configurations. """

    def __init__(
        self,
        name: str,
        bodies: List[Body],
        t: int,
        dt: int = 1000,
        ascii_name: str = None,
    ):
        """
        Construct an Orbit configuration.

        Args:
            name: Name of the orbit
            bodies: List[Body]
            t: time period over which to calculate orbit paths
            dt: time step to use in integration
            ascii_name:
        """
        self.name = name
        self.t = t
        self.dt = dt
        self.ascii_name = ascii_name

        if len(bodies) < 2:
            raise ValueError(
                f"Orbit configuration requires at least 2 bodies, "
                f"{len(bodies)} supplied"
            )
        else:
            self.bodies = bodies


# TODO: set dt in the Orbit configuration also
BROUCKE_A_2 = Orbit(
    name="BROUCKE_A_2",
    bodies=[
        Body(x=0.3361300950, y=0.0, vx=0.0, vy=1.5324315370, mass=1, name="Body 1",),
        Body(x=0.7699893804, y=0.0, vx=0.0, vy=-0.6287350978, mass=1, name="Body 2",),
        Body(x=-1.1061194753, y=0.0, vx=0.0, vy=-0.9036964391, mass=1, name="Body 3",),
    ],
    t=8,
    dt=1000,
    ascii_name="""
    .______   .______       ______    __    __    ______  __  ___  _______         ___          ___   
    |   _  \  |   _  \     /  __  \  |  |  |  |  /      ||  |/  / |   ____|       /   \        |__ \  
    |  |_)  | |  |_)  |   |  |  |  | |  |  |  | |  ,----'|  '  /  |  |__         /  ^  \          ) | 
    |   _  <  |      /    |  |  |  | |  |  |  | |  |     |    <   |   __|       /  /_\  \        / /  
    |  |_)  | |  |\  \----|  `--'  | |  `--'  | |  `----.|  .  \  |  |____     /  _____  \      / /_  
    |______/  | _| `._____|\______/   \______/   \______||__|\__\ |_______|   /__/     \__\    |____|
    """,
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
    ascii_name="""
    .______    __    __  .___________.___________._______ .______      _______  __      ____    ____     __  ____    ____ 
    |   _  \  |  |  |  | |           |           |   ____||   _  \    |   ____||  |     \   \  /   /    |  | \   \  /   / 
    |  |_)  | |  |  |  | `---|  |----`---|  |----|  |__   |  |_)  |   |  |__   |  |      \   \/   /     |  |  \   \/   /  
    |   _  <  |  |  |  |     |  |        |  |    |   __|  |      /    |   __|  |  |       \_    _/      |  |   \      /   
    |  |_)  | |  `--'  |     |  |        |  |    |  |____ |  |\  \----|  |     |  `----.    |  |        |  |    \    /    
    |______/   \______/      |__|        |__|    |_______|| _| `._____|__|     |_______|    |__|        |__|     \__/     
    """,
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
    ascii_name="""
     _______  .______          ___       _______   ______   .__   __.  _______  __      ____    ____     __   __      __   _____          ___      
    |       \ |   _  \        /   \     /  _____| /  __  \  |  \ |  | |   ____||  |     \   \  /   /    |  | |  |    /_ | | ____|        /   \     
    |  .--.  ||  |_)  |      /  ^  \   |  |  __  |  |  |  | |   \|  | |  |__   |  |      \   \/   /     |  | |  |     | | | |__         /  ^  \    
    |  |  |  ||      /      /  /_\  \  |  | |_ | |  |  |  | |  . `  | |   __|  |  |       \_    _/      |  | |  |     | | |___ \       /  /_\  \   
    |  '--'  ||  |\  \----./  _____  \ |  |__| | |  `--'  | |  |\   | |  |     |  `----.    |  |        |  | |  |     | |  ___) |     /  _____  \  
    |_______/ | _| `._____/__/     \__\ \______|  \______/  |__| \__| |__|     |_______|    |__|        |__| |__|     |_| |____/     /__/     \__\ 
    """,
)

TWO_LIGHT_ONE_MASSIVE = Orbit(
    name="TWO_LIGHT_ONE_MASSIVE",
    bodies=[
        Body(x=-50, y=0, vx=0, vy=-10, mass=50, name="Light Body 1"),
        Body(x=0, y=0, vx=0, vy=0, mass=3000, name="Massive Body"),
        Body(x=50, y=0, vx=0, vy=10, mass=50, name="Light Body 2"),
    ],
    t=204,
    ascii_name="""
     ___       __       __    _______  __    __  .___________.    __     .___  ___.      ___           _______.     _______. __  ____    ____  _______ 
    |__ \     |  |     |  |  /  _____||  |  |  | |           |   /_ |    |   \/   |     /   \         /       |    /       ||  | \   \  /   / |   ____|
       ) |    |  |     |  | |  |  __  |  |__|  | `---|  |----`    | |    |  \  /  |    /  ^  \       |   (----`   |   (----`|  |  \   \/   /  |  |__   
      / /     |  |     |  | |  | |_ | |   __   |     |  |         | |    |  |\/|  |   /  /_\  \       \   \        \   \    |  |   \      /   |   __|  
     / /_     |  `----.|  | |  |__| | |  |  |  |     |  |         | |    |  |  |  |  /  _____  \  .----)   |   .----)   |   |  |    \    /    |  |____ 
    |____|    |_______||__|  \______| |__|  |__|     |__|         |_|    |__|  |__| /__/     \__\ |_______/    |_______/    |__|     \__/     |_______|
    """,
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
    ascii_name="""
    ____    ____  __  .__   __.   _______    ____    ____  ___      .__   __.   _______     ___   .______   
    \   \  /   / |  | |  \ |  |  /  _____|   \   \  /   / /   \     |  \ |  |  /  _____|   |__ \  |   _  \  
     \   \/   /  |  | |   \|  | |  |  __      \   \/   / /  ^  \    |   \|  | |  |  __        ) | |  |_)  | 
      \_    _/   |  | |  . `  | |  | |_ |      \_    _/ /  /_\  \   |  . `  | |  | |_ |      / /  |   _  <  
        |  |     |  | |  |\   | |  |__| |        |  |  /  _____  \  |  |\   | |  |__| |     / /_  |  |_)  | 
        |__|     |__| |__| \__|  \______|        |__| /__/     \__\ |__| \__|  \______|    |____| |______/  
    """,
)
