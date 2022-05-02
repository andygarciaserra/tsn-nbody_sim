#IMPORTING PACKAGES:
import os
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy import pi
import h5py
import sys
from classes import universe,particle
import random




#CREATING A TEST UNIVERSE OF N=1000:

u = universe(1,10,10)
u.whole(10)
