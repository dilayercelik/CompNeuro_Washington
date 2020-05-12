# -*- coding: utf-8 -*-
"""
Created on Tue May 12 15:13:11 2020

@author: Dilay Ercelik
"""

import numpy as np
import matplotlib.pyplot as plt
import pickle


# Question 7
print('Question 7:', '\n')

with open('tuning_3.4.pickle', 'rb') as f:
    data = pickle.load(f)
    
    
stim = data['stim']

n1 = np.array(data['neuron1'])
n2 = np.array(data['neuron2'])
n3 = np.array(data['neuron3'])
n4 = np.array(data['neuron4'])

mean_firing_rate_n1 = np.average(n1, axis = 0)
mean_firing_rate_n2 = np.average(n2, axis = 0)
mean_firing_rate_n3 = np.average(n3, axis = 0)
mean_firing_rate_n4 = np.average(n4, axis = 0)



# Visualisations for Question 7

# Plots the tuning curve for neuron n1:
plt.figure(1)

plt.subplot(221)  # 2 rows, 2 colums, subplot in position 1 (221)
plt.title('Tuning curve of neuron n1')
plt.xlabel('stimulus (stim)')
plt.ylabel('mean firing rate')
plt.plot(stim, mean_firing_rate_n1)

# Plots the tuning curve for neuron n2
plt.subplot(222)
plt.title('Tuning curve of neuron n2')
plt.xlabel('stimulus (stim)')
plt.ylabel('mean firing rate')
plt.plot(stim, mean_firing_rate_n2)

# Plots the tuning curve for neuron n3
plt.subplot(223)
plt.title('Tuning curve of neuron n3')
plt.xlabel('stimulus (stim)')
plt.ylabel('mean firing rate')
plt.plot(stim, mean_firing_rate_n3)

# Plots the tuning curve for neuron n4
plt.subplot(224)
plt.title('Tuning curve for neuron n4')
plt.xlabel('stimulus (stim)')
plt.ylabel('mean firing rate')
plt.plot(stim, mean_firing_rate_n4)

# Answer to Question 7:
# "Half-Wave rectified cosine



# Question 8
print('Question 8', '\n')

# If a distribution is Poisson, the variance AND the mean of data are EQUAL
# so if variance - mean is very far from 0, 
# then the distribution must be different from a Poisson distribution

# note: we have the firing rate of each neuron (for various stim values), not the spike count:
# firing rate = spike count / time interval 
# because time interval = 10s for each recording, spike count = firing rate * 10 
# e.g. for neuron n1: spike count = n1 * 10

diff_n1 = 10 * np.var(n1, axis = 0) - np.average(n1, axis = 0)
diff_n2 = 10 * np.var(n2, axis = 0) - np.average(n2, axis = 0)
diff_n3 = 10 * np.var(n3, axis = 0) - np.average(n3, axis = 0)
diff_n4 = 10 * np.var(n4, axis = 0) - np.average(n4, axis = 0)


# Visualisations
plt.figure(2)

plt.plot(stim, diff_n1, label = "n1")
plt.plot(stim, diff_n2, label = "n2")
plt.plot(stim, diff_n3, label = "n3")
plt.plot(stim, diff_n4, label = "n4")

plt.legend()

# Observation of plot 2: Neuron n3 spike distribution seems VERY different 
# from the distributions of other neurons (n1, n2, n4)

# Answer to Question 8:
# "Neuron 3"

