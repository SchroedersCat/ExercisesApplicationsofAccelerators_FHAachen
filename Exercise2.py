# Exercise 2 Application of Accelerators
#Joel Piechotka; 21.10.2020
#Contact: Joel.Piechotkalumni.fh-aachen.de

import numpy as np
import scipy.constants as sc
import matplotlib.pyplot as plt

# Task 4: Calculate the lentht of the first 20 segments of the Wideröe structure of a accelerator for medical applications (C-12)

phase=3*np.pi/8
frequency=100*10**6 # in Hz
voltage=100*10**3 # in V

q=6*sc.e #charge of 12-c 6+ ions 


def l_i(i, hf, psi_r, u0):
    """calculates the lengths of each i-th element of the Wideröe structure"""
    l_i=1/hf*np.sqrt(i*q*u0*np.sin(psi_r)/(2*sc.m_p))
    return l_i

len_of_segments=np.vectorize(l_i)

print("Length li in m:")
len_array=len_of_segments([np.arange(1,21,1)], frequency, phase, voltage)

print(len_array)
total_length=np.sum(len_array)

print("Summed length of segments of the Wideröe structure: ", np.round(total_length, 2), " m")