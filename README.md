# n-body-simulation
This repository contains the classes for a n-body gravitational simulation (newtonian) created with Python.

The files contained are the following:

'Particle.py' file containing the class called 'Particle', where the properties of the planets are defined.

'solarsystem.py' file containing the class called 'solarsystem', where the properties defines in the 
'Particle' class are calculated. It's the main bit of code of the whole folder.

'solarsystemtest.py' file containing the initial conditions of the planets and the loop that updates them
and saves the updated information on a file called 'solarsystemanalysis'.

'Analysis.py' file opens the file called 'solarsystemanalysis' and appends the data in arrays that are 
then plotted.

'Report.pdf' file is a wider description of the code and its purpose.
