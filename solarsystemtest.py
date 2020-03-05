from solarsystem import solarsystem
from Particle import Particle
import numpy as np 
import math
import matplotlib.pyplot as plt 
import copy

"""
This file uses 'Particle' class to define planets' initial conditions and reiterates the calculations defined in the methods of 'solarsystem' class,
which allows the properties defined in 'Particle' class to be updated and added at every 'deltaT' time step.
"""

planet1 = Particle(np.array([0., 0., 0.]), np.array([0., 0., 0.]), np.array([0., 0., 0.]), 'Sun', 1988500e24, 0., np.array([0.,0.,0.]))
planet2 = Particle(np.array([0.2010056011166326*149597870700, 0.2405381641244316*149597870700,0.001215319644815392*149597870700]), np.array([-0.02717021227155681*149597870700/86400, 0.01920474190026218*149597870700/86400 , 0.004061830215553290*149597870700/86400]), np.array([0.,0.,0.]),'Mercury', 3.302e23, 0., 0.)
planet3 = Particle(np.array([1.041103562598392e-1*149597870700, 7.125879298520844e-1*149597870700,3.769579221159655e-3*149597870700]), np.array([-2.008234036373941e-2*149597870700/86400, 2.822450066512053e-3*149597870700/86400 , 1.197633126564550e-3*149597870700/86400]), np.array([0.,0.,0.]),'Venus', 48.685e23, 0., 0.)
planet4 = Particle(np.array([1.328200666822997*149597870700, 4.884221263602231e-01 *149597870700,-2.235667651482616e-02*149597870700]), np.array([-4.295630759622566e-3*149597870700/86400, 1.432939645000289e-2 *149597870700/86400 , 4.056648446684463e-4*149597870700/86400]), np.array([0.,0.,0.]),'Mars', 6.4171e23, 0., 0.)
planet5 = Particle(np.array([4.418063201337957e-1*149597870700, 8.825675035318287e-1 *149597870700,-4.058220747321861e-5*149597870700]), np.array([-1.565783645780632e-2*149597870700/86400, 7.637704681700348e-3 *149597870700/86400 , -9.413648096658849e-7*149597870700/86400]), np.array([0.,0.,0.]),'Earth', 5.97219e24, 0., 0.)
planet6 = Particle(np.array([4.413736897286364e-1*149597870700, 8.849797486240868e-1 *149597870700,-1.071145509737709e-4*149597870700]), np.array([-1.626494417604724e-2*149597870700/86400, 7.526501615526697e-3 *149597870700/86400 , 5.179658294175649e-5*149597870700/86400]), np.array([0.,0.,0.]),'Moon', 7.349e22, 0., 0.)
planet7 = Particle(np.array([-2.377572473255078*149597870700, -4.803513511729565*149597870700,7.315016995280497e-2*149597870700]), np.array([6.678206725705267e-3*149597870700/86400, -2.994174867655442e-3 *149597870700/86400 , -1.369682395491331e-4*149597870700/86400]), np.array([0.,0.,0.]),'Jupiter', 1898.13e24, 0., 0.)
planet8 = Particle(np.array([1.773015428595688*149597870700, -9.903687140993407*149597870700,1.015790883658452e-1*149597870700]), np.array([5.192524619974341e-3*149597870700/86400, 9.639453586249255e-4 *149597870700/86400 , -2.235700157856848e-4*149597870700/86400]), np.array([0.,0.,0.]),'Saturn', 5.6834e26, 0., 0.)
planet9 = Particle(np.array([17.089472788338050*149597870700, 10.12824310001378*149597870700,-1.836816640528774e-1*149597870700]), np.array([-2.027370263682365e-3*149597870700/86400, 3.19724816985324e-3 *149597870700/86400 , 3.813919921892789e-5*149597870700/86400]), np.array([0.,0.,0.]),'Uranus', 86.813e24, 0., 0.)
planet10 = Particle(np.array([28.95440762036375*149597870700, -7.598597867622669*149597870700,-5.108805151298627e-1*149597870700]), np.array([7.833559822225717e-4*149597870700/86400, 3.052883433361287e-3 *149597870700/86400 , -8.132207400564762e-5*149597870700/86400]), np.array([0.,0.,0.]),'Neptune', 102.413e24, 0., 0.)
planets = planet1, planet2, planet3, planet4, planet5, planet6, planet7, planet8, planet9, planet10
sol = solarsystem(planets) # sol gathers all the information obtained about each planet of the system (position, velocity,...) at each deltaT.


time = 0 
deltaT = 86400 # time step in which we assume the calculated properties to be constant, defined.
Data = [] #this contains all the information of each planet at each step considered.

N=10000 # number of recalculations (updates).
for num in range (0,N): # this loop updates all the the info of each planet (again: velocity, position,...) for each time step, from time=0.
    time = time + num*deltaT
    sol.VelPlanet(deltaT)
    sol.PosPlanet(deltaT)
    #sol.VelPlanet(deltaT)
    sol.AccPlanet()
    sol.momentum()
    sol.kin_energy()
    item=[time, copy.deepcopy(sol)] # array that contains 'time' at [0] and each planet's info (as defined in the 'Partice' class) at [1]
    Data.append(item) # appends all info in 'item' to the 'Data' array
np.save("solarsystemanalysis",Data) #this saves all the info contained in 'Data' in a file called 'solarsystemanalysis', then analysed in the 'Analysis' program.
    


print(Data)


