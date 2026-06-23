# Physics-in-Python
Projects that include the use of python to explain, verify and simulate various concepts of Physics.

This project shows the trajectory of a ball thrown upwards at an initial velocity (u) of 20 m/s. We take the acceleration as the gravitational constant (g), which acts towards the surface of earth, and in this case, opposite to the direction of the initial force (the ball being thrown upwards). I used the linspace function to generate random time points from 0 to 5 seconds. The displacement at each point is calculated by the variable 's_value'. It plugs in the value of initial speed and time (when used) to the formula I found for displacement by integration of acceleration, and then of velocity (v). 

NOTE: Does not consider air resistance or drag.