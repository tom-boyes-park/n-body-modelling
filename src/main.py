from src.config import DefaultConditions
from src.orbits import calc_orbits, plot_orbits

import logging


def initialise_logger():
    logging.basicConfig(
        format="%(levelname)s %(asctime)s %(filename)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logging.root.setLevel(logging.DEBUG)


if __name__ == "__main__":
    initialise_logger()

    bodies = DefaultConditions.YING_YANG_2B.value
    orbits = calc_orbits(bodies=bodies, t0=0, t1=60, dt=5000)

    plot_orbits(orbit_paths=orbits)
