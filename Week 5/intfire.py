from __future__ import print_function
"""
Created on Wed Apr 22 16:02:53 2015

Basic integrate-and-fire neuron 
R Rao 2007

translated to Python by rkp 2015
"""

# For Questions 16-17

import numpy as np
import matplotlib.pyplot as plt


# input current
I = 250 # nA  # initial value = 1

# capacitance and leak resistance
C = 1 # nF
R = 40 # M ohms

# I & F implementation dV/dt = - V/RC + I/C
# Using h = 1 ms step size, Euler method

V = 0
tstop = 200
abs_ref = 5 # absolute refractory period 
ref = 0 # absolute refractory period counter
V_trace = []  # voltage trace for plotting
V_th = 10 # spike threshold

for t in range(tstop):
  
   if not ref:
       V = V - (V/(R*C)) + (I/C)
   else:
       ref -= 1
       V = 0.2 * V_th # reset voltage
   
   if V > V_th:
       V = 50 # emit spike
       ref = abs_ref # set refractory counter

   V_trace += [V]


plt.plot(V_trace)
plt.show()


# Question 16
# Answer: when I = 250


# Question 17
# Answer: there are 34 spikes when I = 250 nA (method: I counted the 'peaks' on the plot')
# AND firing rate = spike count / trial duration
# and in the plot, we can see 34th spike at 200ms (x axis limit) so trial duration = 200
# firing rate = 34/200 = 0.17 spike/ms 
# because answer is asked in Hz, we have to convert from ms to s (trial duration)
# so multiply 0.17 by 1000:
# and finally: I = 170 Hz

