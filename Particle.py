import numpy as np

class Particle:

    """
    This class in called 'Particle'. Its main aim is to define the properties we want to analyze about the bodies in the system.
    The main variables (called inside Particle class through 'self') are defined as:
    position = position x,y,z of a body. It is defined through an array.
    velocity = velocity x,y,z of a body. It is defined through an array.
    acceleration = acceleration x,y,z of a body. It is defined through an array.
    Name = name of the body in the system
    mass = mass of the body in the system 
    kenergy = kinetic energy of each body in the system 
    momentum = linear momentum of each body in the system 
    """
    position=np.array([0., 0., 0.])
    velocity=np.array([0., 0., 0.])
    acceleration=np.array([0., 0., 0.])
    Name='Body'
    mass=0.
    kenergy= 0.
    momentum=0.
    
    

    def __init__(self, initialPosition, initialVelocity, initialAcceleration, Name, mass, kenergy, momentum):

        """ 
        'init' is the initialisation method, it defines the initial conditions (position, velocity, acceleration) of the system's bodies we are going 
        to analyze; 'self' is a 'dummy' variable which allows to distinguish between te variables defined at the beginning and the ones of the 'init'
        method. It also fills with any argument we want, in this case:
        initialPosition
        initialVelocity
        initialAcceleration
        """

        self.velocity=initialVelocity
        self.position=initialPosition
        self.acceleration=initialAcceleration
        self.Name=Name
        self.mass=mass
        self.kenergy
        self.momentum


    def __repr__(self):

        """
        This method called 'repr' controls what we print whenever we use a print statement
        """
        return 'Particle: %10s, Mass: %.5e, Position: %s, Velocity: %s, Acceleration:%s'  %(self.Name,self.mass,self.position, self.velocity,self.acceleration)

