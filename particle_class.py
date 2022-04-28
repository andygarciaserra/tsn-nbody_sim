#IMPORTING PACKAGES:
import os
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy import pi
import h5py
import sys
import particle_class





# Particle class:
class particle:
    xpos = 0
    ypos = 0
    vx = 0
    vy = 0
    
    def __init__(self,x,y,xvel,yvel):
        self.xpos = x
        self.ypos = y
        self.vx = xvel
        self.vy = yvel
        
    def pos(self):
        return np.array([xpos,ypos])
    def vel(self):
        return np.array([vx,vy])

    
    

    
# Universe class:
class universe:
    particles = np.array([])
    
    def __init__(self,N,Lx,Ly):
        for i in range(N):
            x = np.random.randint(Lx)
            y = np.random.randint(Ly)
            xvel = np.random.uniform(-1,1)
            yvel = sqrt(1-xvel**2)
            part = particle(x,y,xvel,yvel)
            self.particles = np.concatenate(particles,part)
        
    def add(self,part):
        particles = part.append(part)
    def plot(self):
        plt.plot()