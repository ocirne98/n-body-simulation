from solarsystem import solarsystem
from Particle import Particle
import numpy as np 
import math
import matplotlib.pyplot as plt 
import copy

"""
The main aim of this program is plotting and analysing the Data obtained in the 'solarsystemtest' file, to see how the simulation is behaving.
"""

Data = np.load("solarsystemanalysis.npy", allow_pickle=True) # this loads the info saved in the 'solarsystemanalysis' file.

"""
Arrays that contain the x and y positions to be plotted over time.
"""

x1 = [] #planets' position arrays
y1 = [] 
x2 = [] 
y2 = []
x3 = [] 
y3 = []
x4 = [] 
y4 = []
x5 = [] 
y5 = []
x6 = [] 
y6 = []
x7 = [] 
y7 = []
x8 = [] 
y8 = []
x9 = [] 
y9 = []
x10 = [] 
y10 = []


"""
Arrays that contain the quantities (energy, momentum) to be plotted
"""
y_E = [] #total energy of the system (Virial theorem) for each time step
x_E = []

y_p = [] #total momentum of the system for each time step
x_p = []

P = [] #total momentum of the system for fractional change for each time step
x_P = []


Ene = [] #total energy of the system (Virial theorem) for fractional change for each time step
x_Ene = []


for info in Data:  #loop that appends the data saved in 'Data' for each time step to the arrays defined above.
    
    x1.append(info[1].planets[0].position[0]) #Firstly we take the info in 'position[1]' of 'Data' (all planets' information), then a planet, then its position(x,y or z).
    y1.append(info[1].planets[0].position[1]) #Same thing goes for the others. 'info[0]' is indeed 'time'.

    x2.append(info[1].planets[1].position[0])
    y2.append(info[1].planets[1].position[1])

    x3.append(info[1].planets[2].position[0])
    y3.append(info[1].planets[2].position[1])

    x4.append(info[1].planets[3].position[0])
    y4.append(info[1].planets[3].position[1])
    
    x5.append(info[1].planets[4].position[0])
    y5.append(info[1].planets[4].position[1])
    
    x6.append(info[1].planets[5].position[0])
    y6.append(info[1].planets[5].position[1])
    
    x7.append(info[1].planets[6].position[0])
    y7.append(info[1].planets[6].position[1])
    
    x8.append(info[1].planets[7].position[0])
    y8.append(info[1].planets[7].position[1])
    
    x9.append(info[1].planets[8].position[0])
    y9.append(info[1].planets[8].position[1])

    x10.append(info[1].planets[9].position[0])
    y10.append(info[1].planets[9].position[1])
    
    
    x_E.append(info[0]) 
    y_E.append(info[1].theorem()) #Total Energy at each time (as defined in solarsystem class)

    Ene.append(info[1].theorem()) #This array is then used in list comprehension (see plotting below)
    x_Ene.append(info[0])

    y_p.append(info[1].totalmomentum()) #Total Momentum at each time (as defined in solarsystem class)
    x_p.append(info[0]) 

    P.append(info[1].totalmomentum()) #This array is then used in list comprehension (see plotting below)
    x_P.append(info[0])


    
################################################################################################
################################################################################################
################################################################################################

#ORBITS PLOTS

plt.plot(x1,y1,'r.',label='Sun Trajectory')

plt.plot(x2,y2,'b-', linewidth=0.5,label='Mercury Trajectory')
plt.plot(x3,y3,'g.',linewidth=0.5,label='Venus Trajectory')
plt.plot(x4,y4,'c-',linewidth=0.5,label='Mars Trajectory')
plt.plot(x5,y5,'m-',linewidth=0.5,label='Earth Trajectory')
plt.plot(x6,y6,'y-',linewidth=0.5,label='Moon Trajectory')
plt.plot(x7,y7,'g-',linewidth=0.5,label='Jupiter Trajectory')
plt.plot(x8,y8,'y-',linewidth=0.5,label='Saturn Trajectory')
plt.plot(x9,y9,'r-',linewidth=0.5,label='Uranus Trajectory')
plt.plot(x10,y10,'r-',linewidth=0.5,label='Neptune Trajectory')

plt.xlabel('x-position', fontsize=15)
plt.ylabel('y-position', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(loc=1)
plt.show() 




################################################################################################
################################################################################################
################################################################################################

#PLOTS OF OTHER PROPERTIES

#Total energy plot (Virial theorem)
plt.plot(x_E,y_E,'r-', label='Variation of the Total Energy')
plt.xlabel('Time (s)', fontsize=15)
plt.ylabel('Total Energy of the System (J)', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(loc=1, fontsize=15)
plt.show() 

#Fractional change in total energy plot
plt.plot(x_Ene,np.abs([1-(n/Ene[0]) for n in Ene])*100,'r-', label='Variation of the Energy Fractional Change') #List comprehension is used to divide the total energy in each step (in array 'Ene') by its initial value 'Ene[0]'
plt.xlabel('Time (s)', fontsize=15)
plt.ylabel('Total Energy Fractional Change (%)', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(loc=1, fontsize=15)
plt.show()


#Total momentum plot
plt.plot(x_p,y_p,'r-', label='Variation of the Total Momentum')
plt.xlabel('Time (s)', fontsize=15)
plt.ylabel('Total Momentum of the System (kg x m/s)', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(loc=1, fontsize=15)
plt.show() 

#Fractional change in total momentum plot
plt.plot(x_P,np.abs([1-(n/P[0]) for n in P])*100,'r-',linewidth=0.3, label='Variation of the Energy Fractional Change') #List comprehension is used to divide the total energy in each step (in array 'P') by its initial value 'P[0]'
plt.xlabel('Time (s)', fontsize=15)
plt.ylabel('Total Momentum Fractional Change (%)', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(loc=2, fontsize=15)
plt.show() 

massimo1 = max(np.abs([1-(n/P[0]) for n in P])) #finds momentum fractional change's peak
print (massimo1)

massimo2 = max(np.abs([1-(n/Ene[0]) for n in Ene])) #finds energy fractional change's peak
print (massimo2)



