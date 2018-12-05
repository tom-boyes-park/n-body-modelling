# import requirements
import pandas as pd
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


def set_initial(bodies):
    """

    :param bodies: List of Body classes
    :return: list of starting x, y, vx, and vy values for each Body in bodies
    """
    initial = []

    # Loop through bodies and create initial conditions to be passed into the integrator
    for body in bodies:
        values = [body.x, body.vx, body.y, body.vy]
        initial += values

    return initial


def n_body_func(t, pos_vel_array, bodies):
    """

    Function to be passed into the ode integrator. Tracks the changes in spatial and velocity values.

    :param t: time step
    :param pos_vel_array: array containing x, y, vx and vy values for each body
    :param bodies: list of Body classes
    :return: array containing change in spatial and velocity values for each body
    """

    # pos_vel_array = [body1_x, body1_vx, body1_y, body1_vy, body2_x, ...]

    # Set up array to store updated spatial and velocity values
    dpos_vel_array = np.zeros(4 * len(bodies))

    # Arbitrary value for G (gravitational constant)
    G = 1

    # Change in x, y is velocity in x, y
    dpos_vel_array[0:len(dpos_vel_array):4] = pos_vel_array[1:len(pos_vel_array):4]
    dpos_vel_array[2:len(dpos_vel_array):4] = pos_vel_array[3:len(pos_vel_array):4]

    # Loop through bodies, calculating change in vx, vy due to all other bodies
    for i, body in enumerate(bodies):

        # Extract x, y values of body
        x_pos_body = pos_vel_array[i * 4]
        y_pos_body = pos_vel_array[i * 4 + 2]

        dx_vel_body = 0
        dy_vel_body = 0

        for j, other_body in enumerate(bodies):

            # Check bodies aren't the same
            if i != j:
                # Extract x, y & mass of other body
                x_pos_other_body = pos_vel_array[j * 4]
                y_pos_other_body = pos_vel_array[j * 4 + 2]
                mass_other_body = other_body.mass

                # Distance
                r = ((x_pos_body - x_pos_other_body) ** 2 + (y_pos_body - y_pos_other_body) ** 2) ** 0.5

                # Change in vx, vy
                dx_vel_body += (-G * mass_other_body * (x_pos_body - x_pos_other_body)) * r ** (-3)
                dy_vel_body += (-G * mass_other_body * (y_pos_body - y_pos_other_body)) * r ** (-3)

        # Add resultant change in vel to array
        dpos_vel_array[i * 4 + 1] = dx_vel_body
        dpos_vel_array[i * 4 + 3] = dy_vel_body

    return dpos_vel_array


def calc_orbits(bodies, t0, t1, dt):
    """

    :param bodies: List of Body classes that describe the starting conditions and masses of the bodies
    bodies due to the gravitational forces from other bodies at each time step
    :param t0: Start time
    :param t1: End time
    :param dt: Time step (seconds)
    :return: Array containing spatial coordinates and velocities of bodies at each time step
    """

    # Initial conditions (x, vx, y, vy)
    initial = set_initial(bodies=bodies)

    # Time period over which to calculate orbit paths
    t = np.linspace(t0, t1, dt)

    # Array for solution
    y = np.zeros((len(t), len(bodies) * 4))

    # Initial value of array
    y[0, :] = initial

    # Setup integrator
    integrator = integrate \
        .ode(n_body_func) \
        .set_integrator('dop853', rtol=1e-6, atol=1e-10) \
        .set_initial_value(initial, t0) \
        .set_f_params(bodies)

    # Iterate over time intervals and integrate, storing updated spatial coordinates and velocities of bodies
    print("Calculating orbits")
    for i in range(1, len(t)):
        y[i, :] = integrator.integrate(t[i])

    return y


def plot_orbits(orbit_paths, fig_name=None):
    """

    :param orbit_paths: array containing spatial and velocity values over time
    :param fig_name: if string provided, png of plot will be saved as name given
    :return:
    """

    plt.figure(figsize=(15, 15))

    for i in range(int(orbit_paths.shape[1] / 4)):
        plt.plot(orbit_paths[:, i * 4], orbit_paths[:, i * 4 + 2])

    if fig_name is not None:
        plt.savefig("src/plots/{}.png".format(fig_name))

    return


def store_orbits(bodies, orbit_paths, file_name):
    """

    :param bodies: List of Body classes
    :param orbit_paths: array containing spatial and velocity values over time
    :param file_name: name of csv file that will store orbit path data
    :return:
    """

    # Put orbits array in pandas DataFrame
    orbits_df = pd.DataFrame(orbit_paths)

    # Add column names
    for i in range(len(bodies)):
        body_name = bodies[i].name

        rename_spec = {
            i * 4: body_name + '_x',
            i * 4 + 1: body_name + '_vx',
            i * 4 + 2: body_name + '_y',
            i * 4 + 3: body_name + '_vy'
        }

        orbits_df.rename(columns=rename_spec, inplace=True)

    orbits_df.to_csv("src/data/{}.csv".format(file_name), index=None)
