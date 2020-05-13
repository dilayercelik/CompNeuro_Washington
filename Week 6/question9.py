# -*- coding: utf-8 -*-
"""
Created on Wed May 13 12:40:49 2020

@author: Dilay Ercelik
"""

# FOR QUESTION 9 OF QUIZ 6

import numpy as np

# our network's weight matrix W:
W = np.array([
    [ 0.6, 0.1, 0.1, 0.1, 0.1 ],
    [ 0.1, 0.6, 0.1, 0.1, 0.1 ],
    [ 0.1, 0.1, 0.6, 0.1, 0.1 ],
    [ 0.1, 0.1, 0.1, 0.6, 0.1 ],
    [ 0.1, 0.1, 0.1, 0.1, 0.6 ]
    ])


# a static input vector u:
u = np.array([
    [0.6],
    [0.5],
    [0.6],
    [0.2],
    [0.1] 
    ])

# a recurrent weight matrix M:
M = np.array([
    [ -0.75, 0, 0.75, 0.75, 0 ],
    [ 0, -0.75, 0, 0.75, 0.75 ], 
    [ 0.75, 0, -0.75, 0, 0.75 ],
    [ 0.75, 0.75, 0, -0.75, 0 ],
    [ 0, 0.75, 0.75, 0, -0.75 ] 
    ])



# Calculating the steady state output v_ss of the network
print('The formula of the steady state ouput is v_ss = sum((h.e) * e/1-ev)')


# Calculates h:
h = W * u


# Calculates the eigenvectors (e) and their corresponding eigenvalues (ev) of matrix M
ev, e = np.linalg.eig(M)
print(e)


# the steady state output v_ss of the network:
v_ss_without_sum = ( (np.dot(h.T, e)) / (1 - ev) ) * e


v_ss = np.sum(v_ss_without_sum, axis = 0)

print(v_ss)