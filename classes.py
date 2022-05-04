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
    v = 2.5
    vx = 0
    vy = 0

    def __init__(self,x,y,vx,vy):
        self.xpos = x
        self.ypos = y
        self.vx = vx
        self.vy = vy

    def pos(self):
        return print('[x,y]= '+str(np.array([self.x,self.y])))
    
    def vel(self):
        return print('[vx,vy]= '+str(np.array([self.vx,self.vy])))

    
    

    
# Universe class:
class universe:
    part = np.array([])
    frames = np.array([])
    tbin = 0.1
    Lx = 0
    Ly = 0
    v = 2.5

    def __init__(self,N,Lx,Ly):
        self.Lx=Lx
        self.Ly=Ly
        for i in range(N):
            x = random.random()*self.Lx
            y = random.random()*self.Ly
            theta = random.random()*(2*np.pi)
            vx = self.v*np.cos(theta) 
            vy = self.v*np.sin(theta)
            self.part = np.append(self.part,particle(x,y,vx,vy))

    def show(self):
        return self.part
    
    def add(self,newpart):
        self.part = np.append(self.part,newpart)
    
    def plot(self):                              # INTENTAR HACER UNA VASRIABLE BOOL 'YES'/'NO' PARA MOSTRAR O NO
        x = [i.xpos for i in self.part]          # LA FIGURA Y ASÍ PODER JUGAR OCN HACER ANIMACIONES CON WHOLE
        y = [i.ypos for i in self.part]
        plt.xlim((0,self.Lx))
        plt.ylim((0,self.Ly))
        plt.scatter(x,y,marker='.')
        plt.show(block=False)
        plt.pause(.05)
        plt.clf()

    def nextframe(self):
        for i in range(len(self.part)):
            newpartx = self.part[i].xpos + self.part[i].vx * self.tbin
            newparty = self.part[i].ypos + self.part[i].vy * self.tbin
        
        # Border collision:
            if(newpartx<0 or newpartx>self.Lx):
                self.part[i].vx = -self.part[i].vx
                newpartx = self.part[i].xpos + self.part[i].vx * self.tbin
            if(newparty<0 or newparty>self.Ly):  
                self.part[i].vy = -self.part[i].vy 
                newparty = self.part[i].ypos + self.part[i].vy * self.tbin

            self.part[i] = particle(newpartx,newparty,self.part[i].vx,self.part[i].vy)
        return self.part

    def whole(self,t):
        totalt = t
        i = 0
        while i < totalt:
            self.frames = np.append(self.frames,self.part)
            self.part = self.nextframe()
            self.plot()
            i+=self.tbin
        
