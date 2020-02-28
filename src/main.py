from config import DefaultBodies, get_default_bodies
from orbits import calc_orbits, plot_orbits, store_orbits


if __name__ == "__main__":
    bodies = get_default_bodies(DefaultBodies.YING_YANG_2B)
    orbits = calc_orbits(bodies=bodies, t0=0, t1=60, dt=5000)

    plot_orbits(orbit_paths=orbits)
    store_orbits(bodies=bodies, orbit_paths=orbits, file_name="orbits_2light_1massive")
