import argparse
import logging

from src.config import (
    YING_YANG_2B,
    BROUCKE_A_2,
    BUTTERFLY_IV,
    DRAGONFLY_II_15_A,
    TWO_LIGHT_ONE_MASSIVE,
    Orbit,
)
from src.orbits import calc_orbits, plot_orbits

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


def initialise_logger():
    logging.basicConfig(
        format="%(levelname)s %(asctime)s %(filename)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logging.root.setLevel(logging.DEBUG)


def initialise_parser() -> argparse.ArgumentParser:
    """ Create ArgumentParser to parse command line arguments """
    parser = argparse.ArgumentParser(
        description="Calculate and plot the orbits of N bodies",
    )
    parser.add_argument("--orbit", type=str, help="name of orbit to be plotted")
    parser.add_argument(
        "--list-orbits",
        help="lists available orbit names that can be used",
        action="store_true",
    )

    return parser


def parse_and_validate_args(args: argparse.Namespace) -> Orbit:
    """
    Parse the arguments supplied via the command line.

    If --list-orbits supplied, the names of the default Orbit configurations are
    printed and application exits. Otherwise it attempts to return the Orbit
    corresponding the to the value supplied for --orbit.

    Args:
        args: command line arguments

    Returns:
        Orbit corresponding to value specified for --orbit
    """
    if args.list_orbits:
        print("Available default orbit names:\n")
        for orbit_name in DEFAULT_ORBITS.keys():
            print(f"{orbit_name}")
        exit(0)

    orbit = args.orbit
    if not orbit:
        raise ValueError("Orbit name must be specified")

    if orbit not in DEFAULT_ORBITS.keys():
        raise ValueError(f"'{orbit}' not recognised")

    return DEFAULT_ORBITS[orbit]


def run():
    parser = initialise_parser()
    orbit = parse_and_validate_args(args=parser.parse_args())

    orbits = calc_orbits(bodies=orbit.bodies, t0=0, t1=orbit.t, dt=5000)
    plot_orbits(orbit_paths=orbits)


if __name__ == "__main__":
    initialise_logger()
    run()
