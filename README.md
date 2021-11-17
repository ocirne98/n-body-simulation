# n-body-simulation
This repository contains the classes for a n-body gravitational simulation (newtonian) created with Python.

The files contained are the following:

'Particle.py', a file containing the class called 'Particle', where the properties of the planets are defined.

'solarsystem.py', a file containing the class called 'solarsystem', where the properties defined in the 
'Particle' class are calculated.

'solarsystemtest.py', a file containing the initial conditions of the planets and the loop that updates them
and saves the updated information on a file called 'solarsystemanalysis'.

'Analysis.py', a file opens a file called 'solarsystemanalysis' and appends the data in arrays that are 
then plotted and visualized.

'Report.pdf', a file is a wider description of the code and its purpose.

By defining the initial position, velocity and acceleration of each planet in 'solarsystemtest.py', along with the size of each step and number of iterations for the Euler-Cromer algorithm, one can use 'Analysis.py' to plot and visualise the trajectories of the planets and of other Solar System properties.
