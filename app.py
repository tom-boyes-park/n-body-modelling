import streamlit as st

from utils.config import DEFAULT_ORBITS
from utils.orbits import calc_orbits, plot_orbits


def markdown_intro():
    st.title("N Body Modelling")

    st.markdown(
        """This web app allows you to explore the orbits of various pre-defined N body
        configurations ($x$, $y$, $v_x$, $v_y$ and $mass$)."""
    )

    st.markdown(
        """The code makes use of [`scipy.integrate.ode`]
        (https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.ode.html)
        in order to calculate the change in $x$, $y$, $v_x$ and $v_y$ at each given time
        step due to the gravitational forces of all other bodies in the system. The
        integrator used is `dopri835`."""
    )

    st.markdown("Use the sidebar to select and plot one of the orbits.")

    st.markdown(
        """Note: initial starting conditions for `BROUCKE_A_2`, `BUTTERFLY_IV`,
        `DRAGONFLY_II_15_A`, & `YING_YANG_2B` taken from http://three-body.ipb.ac.rs/.
        Paper: _M. Šuvakov and V. Dmitrašinović, Three Classes of Newtonian
        Three-Body Planar Periodic Orbits, Phys. Rev. Lett. 110, 114301 (2013).
        arXiv:1303.0181._"""
    )


def main():
    markdown_intro()

    orbit_selected = st.sidebar.selectbox(
        "Choose orbit to plot.", options=list(DEFAULT_ORBITS.keys())
    )

    plot_button = st.sidebar.button(label="Calculate and plot orbit paths")
    if plot_button:
        st.sidebar.text(f"Calculating orbit paths...")

        orbit = DEFAULT_ORBITS[orbit_selected]
        orbits = calc_orbits(bodies=orbit.bodies, t0=0, t1=orbit.t, dt=orbit.dt)

        plot_orbits(orbits, title=orbit_selected)


if __name__ == "__main__":
    main()
