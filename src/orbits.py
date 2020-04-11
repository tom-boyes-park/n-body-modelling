from typing import List

import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

import logging

from src.config import Body

logger = logging.getLogger(__name__)

# Arbitrary value for G (gravitational constant)
G = 1


def create_initial_conditions(bodies: List[Body]) -> List[int]:
    """

    :param bodies: List of Body classes
    :return: list of starting x, y, vx, and vy values for each Body in bodies
    """
    initial = []

    # Loop through bodies and create initial conditions to be passed into the integrator
    logger.info(f"Creating initial conditions for the {len(bodies)} bodies")
    for body in bodies:
        values = [body.x, body.vx, body.y, body.vy]
        initial += values

    return initial


def calc_2d_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Returns:
        Distance between the 2-dimensional co-ordinates supplied.
    """
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def calc_dvel(c1: float, c2: float, r: float, m2: float) -> float:
    """
    Calculates the change in velocity on a target body due to the gravitational force
    of another body (source body) in a single dimension.

    Args:
        c1: value for target body position in x or y dimension
        c2: value for source body position in x or y dimension
        r: distance between 2 bodies
        m2: mass of the source body

    Returns:
        change in target body velocity (float)
    """
    return (-G * m2 * (c1 - c2)) * r ** (-3)


def n_body_func(t, pos_vel, bodies: List[Body]):
    """

    Function to be passed into the ode integrator. Tracks the changes in spatial and velocity values.

    :param t: time step
    :param pos_vel: array containing x, y, vx and vy values for each body
        [x1, vx1, y1, vy1, x2, ...]
    :param bodies: list of Body classes
    :return: array containing change in spatial and velocity values for each body
    """
    # Set up array to store updated spatial and velocity values
    dpos_dvel = np.zeros(4 * len(bodies))

    # Change in x, y is velocity in x, y
    dpos_dvel[0 : len(dpos_dvel) : 4] = pos_vel[1 : len(pos_vel) : 4]
    dpos_dvel[2 : len(dpos_dvel) : 4] = pos_vel[3 : len(pos_vel) : 4]

    # Loop through bodies, calculating change in vx, vy due to all other bodies
    for i, body in enumerate(bodies):
        # Extract x, y values of body
        x1 = pos_vel[i * 4]
        y1 = pos_vel[i * 4 + 2]

        vx1 = 0
        vy1 = 0
        for j, other_body in enumerate(bodies):
            # Check bodies aren't the same
            if i != j:
                # Extract x, y & mass of other body
                x2 = pos_vel[j * 4]
                y2 = pos_vel[j * 4 + 2]

                # Distance to other body
                r = calc_2d_distance(x1=x1, y1=y1, x2=x2, y2=y2,)

                # Change in x, y
                vx1 += calc_dvel(c1=x1, c2=x2, r=r, m2=other_body.mass)
                vy1 += calc_dvel(c1=y1, c2=y2, r=r, m2=other_body.mass)

        # Add resultant change in vel to array
        dpos_dvel[i * 4 + 1] = vx1
        dpos_dvel[i * 4 + 3] = vy1

    return dpos_dvel


def calc_orbits(bodies, t0, t1, dt):
    """

    :param bodies: List of Body classes that describe the starting conditions and
        masses of the bodies
    bodies due to the gravitational forces from other bodies at each time step
    :param t0: Start time
    :param t1: End time
    :param dt: Time step (seconds)
    :return: Array containing spatial coordinates and velocities of bodies at each
        time step
    """

    # Initial conditions (x, vx, y, vy)
    initial = create_initial_conditions(bodies=bodies)

    # Time period over which to calculate orbit paths
    t = np.linspace(t0, t1, dt)

    # Array for solution
    y = np.zeros((len(t), len(bodies) * 4))
    y[0, :] = initial

    # Setup integrator
    integrator = (
        integrate.ode(n_body_func)
        .set_integrator("dop853", rtol=1e-6, atol=1e-10)
        .set_initial_value(initial, t0)
        .set_f_params(bodies)
    )

    # Iterate over time intervals and integrate, storing updated spatial coordinates
    # and velocities of bodies
    logger.info("Calculating orbits")
    for i in range(1, len(t)):
        y[i, :] = integrator.integrate(t[i])

    return y


def plot_orbits(orbit_paths, fig_name=None):
    """

    :param orbit_paths: array containing spatial and velocity values over time
    :param fig_name: if string provided, png of plot will be saved as name given
    :return:
    """

    plt.figure(figsize=(10, 10))

    for i in range(int(orbit_paths.shape[1] / 4)):
        plt.plot(orbit_paths[:, i * 4], orbit_paths[:, i * 4 + 2])

    if fig_name is not None:
        plt.savefig("src/plots/{}.png".format(fig_name))

    return
