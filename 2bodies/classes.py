#IMPORTING PACKAGES:
import os
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy import pi
import h5py
import sys
import random
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def imscatter(x, y, image, ax=None, zoom=1):
    if ax is None:
        ax = plt.gca()
    try:
        image = plt.imread(image)
    except TypeError:
        # Likely already an array...
        pass
    im = OffsetImage(image, zoom=zoom)
    x, y = np.atleast_1d(x, y)
    artists = []
    for x0, y0 in zip(x, y):
        ab = AnnotationBbox(im, (x0, y0), xycoords='data', frameon=False)
        artists.append(ax.add_artist(ab))
    ax.update_datalim(np.column_stack([x, y]))
    ax.autoscale()
    return artists

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
    
    tbin = 7e5      # Time bin for orbit integration.
    Lx = 0          # Size of the system in x.
    Ly = 0          # Size of the system in y.
    v = 2.5         # Constant speed for initial models.
    fig = ''        # Boolean to make a fig or not ('fig' or whatever)
    figyn = ''      # Boolean to avoid nofig message loop.
    method = ''     # Integration method ('Euler' for Euler method, 'RK2' and 'RK4' for Runge Kutta)
    sys = ''        # System type ('rndm' for random / 'binary' for a binary system)

    #System cosmology (CGS):
    G = 6.67408e-08     # cm^3/g/s^2
    MSUN = 1.98892e33   # g
    UA = 1.49598e13     # cm 
    YEAR = 31557600     # s



    def __init__(self,N,Lx,Ly,method,boolfig,sys):  #Definition example: u = Universe(100, 10 , 10 ,  'RK4' ,'fig','binary')  
        self.fig = boolfig                          #------------------------meaning:[ N , Lx , Ly , method , fig , system ] 
        self.Lx = Lx
        self.Ly = Ly
        self.sys = sys
        self.method = method

        # Creating the actual Universe:
        if self.sys=='rndm':
            for i in range(N):
                x = random.random()*self.Lx
                y = random.random()*self.Ly
                theta = random.random()*(2*np.pi)
                vx = self.v*np.cos(theta)
                vy = self.v*np.sin(theta)
                self.part = np.append(self.part,particle(x,y,vx,vy))
        if self.sys=='binary':
            self.part = np.append(self.part,particle(self.UA,0,0,-(2*np.pi*self.UA)/self.YEAR))
            self.part = np.append(self.part,particle(self.UA*1.5,0,0,-1.02*(2*np.pi*1.5*self.UA)/(1.881*self.YEAR)))
            


    def show(self):
        return self.part
    
    def add(self,newpart):
        self.part = np.append(self.part,newpart)
    
    def plot(self):
        if self.fig=='fig':
                #getting data
            x = [i.xpos/self.UA for i in self.part]
            y = [i.ypos/self.UA for i in self.part]
                #plotting
            plt.plot(0,0,'tab:orange',marker='o',ms=15,alpha=0.5)
            plt.plot(x,y,'ko',ms=3)
            #imscatter(0, 0,'sun.jpg', ax=None, zoom=0.1)
            #imscatter(x[0],y[0],'earth.jpg', ax=None, zoom=0.01)
            #imscatter(x[1],y[1],'mars.png', ax=None, zoom=0.02)
                #formatting plot
            plt.xlim((-2,2))
            plt.ylim((-2,2)) 
            #plt.grid()
                #animating and showing
            plt.show(block=False)
            plt.pause(.0000001)
            plt.clf()
        

        elif(self.figyn==''):
            print('No figure shown, write `True` as fig variable.')
            self.figyn = '.'

    def nextframe(self):
        if (self.method=='Euler'):
            for i in range(len(self.part)):
                newpartx = self.part[i].xpos + self.part[i].vx * self.tbin
                newparty = self.part[i].ypos + self.part[i].vy * self.tbin
                r = np.sqrt(newpartx**2 + newparty**2)
                newpartvx = self.part[i].vx - (self.G*self.MSUN/(r**3)) * newpartx * self.tbin
                newpartvy = self.part[i].vy - (self.G*self.MSUN/(r**3)) * newparty * self.tbin
                self.part[i] = particle(newpartx,newparty,newpartvx,newpartvy)
            return self.part

        if (self.method=='RK2'):
            print('RK2 method applied')
                
        if (self.method=='RK4'):
            print('RK4 method applied')

    def twobodies(self,t):
        totalt=t
        i=0
        print(self.show())
        while i < totalt:
            self.frames = np.append(self.frames,self.part)
            self.part = self.nextframe()
            self.plot()
            i+=self.tbin

    def whole(self,t):
        totalt = t
        i = 0
        u.show()
        while i < totalt:
            self.frames = np.append(self.frames,self.part)
            self.part = self.nextframe()
            self.plot()
            i+=self.tbin

