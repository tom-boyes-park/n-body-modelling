from src.config import DefaultConditions
from src.orbits import calc_orbits, plot_orbits


if __name__ == "__main__":
    bodies = DefaultConditions.YING_YANG_2B
    orbits = calc_orbits(bodies=bodies, t0=0, t1=60, dt=5000)

    plot_orbits(orbit_paths=orbits)
