import logging
from argparse import ArgumentParser, Namespace

from utils.config import DEFAULT_ORBITS
from utils.orbits import animate_orbits, calc_orbits, plot_orbits

logger = logging.getLogger(__name__)


def initialise_logger():
    logging.basicConfig(
        format="%(levelname)s %(asctime)s %(filename)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logging.root.setLevel(logging.DEBUG)


def parse_args() -> Namespace:
    """ Parse command line arguments """
    parser = ArgumentParser(description="Calculate and plot the orbits of N bodies",)
    parser.add_argument(
        "--orbit",
        type=str,
        required=True,
        help="Name of pre-defined orbit to be plotted/animated.",
        choices=list(DEFAULT_ORBITS.keys()),
    )
    parser.add_argument(
        "--animate",
        help="Animate the orbit paths.",
        action="store_true",
        required=False,
    )

    return parser.parse_args()


def run():
    args = parse_args()
    logger.info(f"Running with followings args: {args}")

    orbit = DEFAULT_ORBITS[args.orbit]
    orbits = calc_orbits(bodies=orbit.bodies, t0=0, t1=orbit.t, dt=orbit.dt)

    if args.animate:
        animate_orbits(orbits)
    else:
        plot_orbits(orbits)


if __name__ == "__main__":
    initialise_logger()
    run()
