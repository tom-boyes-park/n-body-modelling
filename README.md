# Gravitational N Body Modelling 2D
Repository for the development of gravitational N body modelling calculations and visualisations.

The code in this repository allows you to experiment with different initial starting conditions (x, y, v<sub>x</sub> and v<sub>y</sub>) for N bodies and explore the orbits they follow.

The code makes use of [````scipy.integrate.ode````](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.ode.html) in order to calculate the change in x, y, v<sub>x</sub> and v<sub>y</sub> at a given time step due to the gravitational forces of all other bodies in the system. The integrator used is ````dopri835````.

## Example Orbits
<table>
  <tr>
    <td>Chaos</td>
    <td>2 Light 1 Massive</td>
    <td>Broucke A 2 [1]</td>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/TBoyesPark23/n-body-modelling/blob/master/src/plots/3_body_chaos.png">
    </td>
    <td>
      <img src="https://github.com/TBoyesPark23/n-body-modelling/blob/master/src/plots/orbits_2light_1massive.png">
    </td>
    <td>
      <img src="https://github.com/TBoyesPark23/n-body-modelling/blob/master/src/plots/Broucke_A_2.png">
    </td>
  </tr>
  <tr>
    <td>YIN-YANG 2b [1]</td>
    <td>BUTTERFLY IV [1]</td>
    <td>II.15.A [1]</td>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/TBoyesPark23/n-body-modelling/blob/master/src/plots/YIN-YANG 2b.png">
    </td>
    <td>
      <img src="https://github.com/TBoyesPark23/n-body-modelling/blob/master/src/plots/BUTTERFLY IV.png">
    </td>
    <td>
      <img src="https://github.com/TBoyesPark23/n-body-modelling/blob/master/src/plots/II.15.A.png">
    </td>
  </tr>
</table>

[1] Initial starting conditions taken from http://three-body.ipb.ac.rs/. Paper: <i>M. Šuvakov and V. Dmitrašinović, Three Classes of Newtonian Three-Body Planar Periodic Orbits, Phys. Rev. Lett. 110, 114301 (2013). arXiv:1303.0181.</i>

## How To Use
<ul>
  <li>Clone this repository</li>
  <li>Edit config.json specifying the starting conditions and masses of the bodies. Each body is described by a dictionary which must follow the structure below.</li>
</ul>

````
{
  "name:" "body_name",
  "x": 0,
  "y": 0,
  "vx": 1,
  "vy": 1,
  "mass: "10
}
````
<ul>
  <li>In calc_orbits() in main.py set the desired end time, t1, and number of time steps, dt, for the orbit calculations.</li>
  <li>If you want a .png file saved of the orbits, the file_name parameter must be set in plot_orbits(). </li>
  <li>Run main.py</li>
</ul>
