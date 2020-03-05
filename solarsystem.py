from Particle import Particle
import numpy as np
import math
from matplotlib import pyplot as plt 

class solarsystem :

    """
    We are creating a new class called 'solarsystem'. Its main aim is to calculate the properties we want to analyze about the bodies in the system.
    """

    
    def __init__ (self, planets):

        """
        The initialisation method '__init__' defines the variables ('planets' and 'self') that can be used in
        this class, in each method.  
        """
        self.planets = planets

    
        
    def VelPlanet (self, deltaT):

        """
        In the method 'VelPlanet' the 'for loop' loops over the planets contained in 'self.planet', calculating the velocity 
        for each of them at every time step 'deltaT'.'planet' is the variable assigned to each of planets given when it gets looped over. 
        """

        for planet in self.planets:
            velocity = planet.velocity + (planet.acceleration * deltaT)
            planet.velocity = velocity #Each body's resulting velocity is updated to the body's information defined in the Particle class.
            


    def PosPlanet (self, deltaT): 

        """
        In the method 'PosPlanet' the 'for loop' loops over the planets contained in 'self.planet', calculating the position 
        for each of them at every time step 'deltaT. 'planet' is the variable assigned to each of planets given when it gets looped over. 
        """

        for planet in self.planets:
            position = planet.position + (planet.velocity * deltaT)
            planet.position = position  #Each body's resulting position is updated to the body's information defined in the Particle class.
            
        



    def AccPlanet (self):

        """
        The method 'AccPlanet' finds the total acceleration on every body of the system, which depends 
        on its mass and respective position to the other bodies.
        """

        for planet_a in self.planets: #This 'for' loop choses a body from self.planets and calls it 'planet_a'

            totalAcceleration = np.array([0, 0, 0],dtype=float) #'totalAcceleration' is defined as an array the values of which can be updated, similarly to position and velocity in the Particle class.
            for planet_b in self.planets: #This 'for' loop choses a body from self.planets and calls it 'planet_b'
                if planet_a == planet_b: #This is a condition to avoid to loop over the same planet finding the acceleration on itself, a physical nonsense"
                    continue
                G=6.67408e-11 #gravitational constant
                acceleration = planet_b.mass * (-G) * ((planet_a.position-planet_b.position))/(np.linalg.norm((planet_a.position-planet_b.position)))**3
                totalAcceleration  += acceleration # this sums all the accelerations acting on planet_a.
            planet_a.acceleration = totalAcceleration #Each body's resulting acceleration is updated to the body's information defined in the Particle class.
            
            """ 
            'acceleration' defines the acceleration between the two bodies chosen by the loops;
            'totalAcceleration' defines the acceleration of all bodies on planet_a,
            it is in fact he sum of all accelerations calculated with the 'acceleration' equation.
            'planet_a.acceleration' updates 'totalAcceleration' to the planet considered for every deltaT time step.
            deltaT is introduced indirectly in this method through the variables 'position' and 'velocity', necessary to compute 'acceleration'
            """
            

    def kin_energy (self):

        """
        kin_energy is a function that contains a for loop that select an element in self.planets calling it planet, a variable used
        to evaluate the kinetic energy of each body through the equation shown.
        Each body's resulting kinetic energy is updated to the planet's information defined in the Particle class.
        """

        for planet in self.planets:
            planet.kenergy = 0.5*planet.mass*((np.linalg.norm(planet.velocity))**2) # every 'kenergy' depends by the body's mass and velocity

    
    def total_kin_energy (self):

        """
        This method computes the total kinetic called 'total_kin' energy of the system of bodies, 
        which depends on each 'kenergy' as defined in the Particle class.
        """
        total = 0. 
        for planet in self.planets: #this loop takes each planet's kinetic energy and sums it with the others.
            total += planet.kenergy # the sum of the kinetic energies
            total_kin= total # system's kinetic energy
        
        return(total_kin)


        


    def tot_pot_energy (self):

        """
        This method computes the total potential energy ('pot_energy') of the system of bodies. 
        It depends on the mass of the bodies and their position with the respect to each other. 
        """

        for planet_a in self.planets: #this loop takes a 'planet_a' in 'self.planets'.
            pot_energy = 0.
            for planet_b in self.planets: #this loop takes a 'planet_b' in 'self.planets'.
                if planet_a == planet_b: #This is a condition to avoid to find the potential energy of a body shared with itself, a physical nonsense".
                    continue
                G=6.67408e-11 #gravitational constant
                energy = ((-G) * (planet_a.mass*planet_b.mass))/(np.linalg.norm((planet_a.position-planet_b.position))) #potential energy of planet_a with each other body.
                pot_energy += energy #all the potential energies acting on planet_a summed together.

        return(pot_energy)
           

            
    def theorem (self):
        """
        This method defines the 'Virial theorem', a conservation law for gravitational systems of n-bodies (see Report for details), 
        it depends on 'total_pot_energy' and 'total_kin_energy' of the system.
        """
        tot_energy = 0.
        tot_energy = 2.0*self.total_kin_energy()-self.tot_pot_energy() # 'tot_energy' is the quantity conserved in the system defined by the Virial theorem.

        return(tot_energy)

    def momentum (self): 

        """
        This method evaluates each body's linear momentum, appending it in the body's information defined in the Particle class.
        The body's momentum depends on its mass and velocity.
        """

        for planet in self.planets: #this loop takes a 'planet' from 'self.planets' and computes it linear momentum.
            planet.momentum = planet.mass * planet.velocity #Each body's resulting momentum is updated to the body's information defined in the Particle class.


    def totalmomentum (self):

        """
        This method computes the total linear momentum of the system, which depends on each body's momentum.
        """
        tot_p=0.
        for planet in self.planets: #this loop takes each 'planet' momentum in 'self.planets' and sums them.
            tot_p += planet.momentum #'tot_p' is the resulting vector of all momenta vectors.
            total_mom = np.linalg.norm(tot_p) #the 'total_mom' is the total linear momentum's magnitude, which is conserved.
        return (total_mom)

     