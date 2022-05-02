#IMPORTING PACKAGES:
import os
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy import pi
import h5py
import sys
import random




# Particle class:
class particle:
    xpos = 0
    ypos = 0
    theta = 0
    v = 2.5

    def __init__(self,x,y,theta):
        self.xpos = x
        self.ypos = y
        self.theta = theta
    


    def pos(self):
        return np.array([self.xpos,self.ypos])
    
    def vel(self):
        return np.array([self.v*np.cos(theta),self.v*np.sin(theta)])

    
    

    
# Universe class:
class universe:
    part = np.array([])
    tbin = 0.1
    Lx = 0
    Ly = 0

    def __init__(self,N,Lx,Ly):
        self.Lx=Lx
        self.Ly=Ly
        for i in range(N):
            x = random.random()*self.Lx
            y = random.random()*self.Ly
            theta = random.random()*(2*np.pi)
            self.part = np.append(self.part,particle(x,y,theta))
    


    def show(self):
        return self.part
    
    def add(self,newpart):
        self.part = np.append(self.part,newpart)
    
    def plot(self):
        x = [i.xpos for i in self.part]
        y = [i.ypos for i in self.part]
        plt.figure()
        plt.plot(x,y,'.')
        plt.xlim((0,self.Lx))
        plt.ylim((0,self.Ly))
        plt.show()

    def nextframe(self):
        newpart = np.array([])
        for i in self.part:
            print([i.xpos,i.ypos,i.v])
            newpartx = i.xpos + (i.v * self.tbin * np.cos(i.theta))
            newparty = i.ypos + (i.v * self.tbin * np.sin(i.theta))
            newparti = particle(newpartx, newparty, i.theta)
            newpart = np.append(newpart, newparti)
        return newpart

    def whole(self,t):
        totalt = t
        i = 0
        while i < totalt:
            self.plot()
            self.part = self.nextframe()
            i+=self.tbin
