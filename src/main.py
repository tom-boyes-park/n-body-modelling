# Import requirements
from src.loaders import load_bodies
from src.orbits import calc_orbits, plot_orbits, store_orbits


if __name__ == '__main__':
    bodies = load_bodies("src/resources/config.json")
    orbits = calc_orbits(bodies=bodies, t0=0, t1=211, dt=1000)

    plot_orbits(orbit_paths=orbits)
    store_orbits(bodies=bodies, orbit_paths=orbits, file_name="orbits_2light_1massive")
