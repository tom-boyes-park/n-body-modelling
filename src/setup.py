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

logger = logging.getLogger(__name__)


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
    parser.add_argument(
        "--animate", help="Animate the orbit paths", action="store_true"
    )

    return parser


def _list_orbits():
    logger.info(f"Valid orbit names: {list(DEFAULT_ORBITS.keys())}")


def validate_args(args: argparse.Namespace):
    """
    Validates values passed via command line
    """
    orbit = args.orbit
    if orbit and (orbit not in DEFAULT_ORBITS.keys()):
        _list_orbits()
        raise ValueError(f"Orbit '{orbit}' not recognised")

    if args.animate and not orbit:
        _list_orbits()
        raise ValueError("--orbit must be supplied in order to animate")

    if not args.list_orbits and not args.animate and not orbit:
        raise ValueError("Parameters missing, use -h or --help for options")


def get_orbit(orbit: str) -> Orbit:
    """
    Return Orbit with name of orbit supplied.

    Returns: Orbit
    """
    return DEFAULT_ORBITS[orbit]
