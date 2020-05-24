import logging

from src.orbits import calc_orbits, animate_orbits, plot_orbits
from src.setup import (
    initialise_logger,
    _list_orbits,
    validate_args,
    initialise_parser,
    get_orbit,
)


logger = logging.getLogger(__name__)


def run():
    parser = initialise_parser()
    args = parser.parse_args()
    validate_args(args)

    if args.list_orbits:
        _list_orbits()
        exit(0)

    orbit = get_orbit(args.orbit)
    logger.info(f"Orbit selected:\n{orbit.ascii_name}\n")

    orbits = calc_orbits(bodies=orbit.bodies, t0=0, t1=orbit.t, dt=1000)

    if args.animate:
        animate_orbits(orbits)
    else:
        plot_orbits(orbits)


if __name__ == "__main__":
    initialise_logger()
    run()
