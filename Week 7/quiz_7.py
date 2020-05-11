# -*- coding: utf-8 -*-
"""
Created on Mon May 11 17:30:16 2020

@author: Dilay Ercelik
"""

import numpy as np
import matplotlib.pyplot as plt
import pickle


# Loads python pickle file
with open('c10p1.pickle', 'rb') as f:
    data = pickle.load(f)
    

c10p1 = data['c10p1']


print('Code for Question 1:', '\n')

# Given the input correlation matrix Q:
Q = np.array([[0.2, 0.1],[0.1, 0.3]])

# Calculates the eigenvalues ev and the eigenvectors e of the matrix Q:
ev, e = np.linalg.eig(Q)

print(ev)
print(e)


# If we allow learning to go on for a long period of time,
# w becomes the principal eigenvector of matrix Q
# i.e. the eigenvector e of Q with the greater corresponding eigenvalue ev

# Finds the index of the greatest eigenvalue of the 2 eigenvectors of Q
max_ev_index = ev.argmax()


# Prints the expected w for a learning for a long period of time
w_long_learning = 2 * e[:, max_ev_index] 

print('If we allow learning to go on for a long period of time, w = {}'.format(w_long_learning))



# Question 1 is not related to Questions 7-8-9

print('Code for Question 7:', '\n')


def normal(data):
    """
    Performs a "zero-mean centering step", or normalisation, on the input data

    Parameters
    ----------
    data : float
        Input data (x, y).

    Returns
    -------
    normal_data : float
        Normalised input data.

    """
    mean = np.mean(data, axis = 0)
    
    normal_data = data - mean
    
    return normal_data


# Creates our_normal_data from the raw data c10p1
our_normal_data = normal(c10p1)


# Visualisation of our_normal_data
# To make sure our transformed data is zero-mean centered
plt.figure(1)
plt.scatter(our_normal_data[:, 0], our_normal_data[:, 1], c = 'r', marker = 'o')
plt.title('Oja\'s rule: data cloud centered around (0,0)')
plt.xlabel('u1 (input 1)')
plt.ylabel('u2 (input 2)')
                     
    
# Implements the update rule for Oja's rule
eta = 1
alpha = 1
delta_t = 0.01

# Creates our random first w value: w_zero
w_zero = w = np.random.rand(2) 

# Implementing the updating rule to update w for a number of iterations (e.g. 500).
# Oja's rule for updating w
for step in np.arange(0, 500, 1):
    
    plt.figure(1)
    u = our_normal_data[np.remainder(step, our_normal_data.shape[0]), :]
    v = u @ w     # @ is used for matrix multiplication
    w = w + delta_t * eta * (v * u - alpha * v * v * w)
    plt.plot(v, marker = '^',  c = 'g')
    plt.plot(w[0], w[1], marker = '*', c = 'b')
   
    


# Calculates the correlation matrix C (formula given in the quiz)
# Because our_normal_data is mean_centered, C is also its covariance matrix.
# our_normal_data.shape[0] gives the number M of lines (the number of samples in our_normal_data)
C = np.dot(our_normal_data.T, our_normal_data) / our_normal_data.shape[0]

# Prints the correlation/covariance matrix C of our_normal_data
print('This is the correlation/covariance matrix C of our mean-centered data (our_normal_data): {}'.format(C), '\n')

# Calculates the eigenvalues ev and the eigenvectors e of the matrix C:
ev, e = np.linalg.eig(C)

# Prints eigenvalues (ev) and eigenvectors (e: 2D vectors) of 
# the correlation matrix C of the mean-centered data (our_normal_data)
print('The eigenvalues of the correlation/covariance matrix C of our_normal_data are {} and {}'.format(ev[0], ev[1]), '\n')

print('The eigenvectors of the correlation/covariance matrix C of our_normal_data are {} and {}'.format(e[0], e[1]), '\n')


# Answer to Question 7:
## "The correlation matrix C has only one principal eigenvector,
## but there two vectors of length 1/alpha that are parallel to this eigenvector.
## w can converge to either of these two vectors."

### Note to myself:
# The eigenvector corresponding to the eigenvalue of largest magnitude is called the principal eigenvector.


    
print('Code for Question 8:', '\n')   

# Creates our_normal_data with adjusted mean: data2, not zero-mean centered
constants = [2, 2]
data2 = our_normal_data + np.tile(constants, (our_normal_data.shape[0], 1))


# Visualisation of data2
plt.figure(2)
plt.scatter(data2[:, 0], data2[:, 1], marker = 'o',  c = 'r')
plt.title('Oja\'s rule: data2 cloud')
plt.xlabel('u1 (input 1)')
plt.ylabel('u2 (input 2)')


# Creates our random first w value for the second data (not zero-mean centered data)
w2 = w_zero 

# Implementing the updating rule to update w for a number of iterations (e.g. 500).
# Oja's rule for updating w
for step in np.arange(0, 500, 1):
    
    plt.figure(2)
    u = data2[np.remainder(step, data2.shape[0]), :]
    v = u @ w2
    w2 = w2 + delta_t * eta * (v * u - alpha * v * v * w2)
    plt.plot(v, marker = '^',  c = 'g')
    plt.plot(w2[0], w2[1], marker = '*',  c = 'b')
    

# Answer to question 8:
## "The two vectors that w (w2) converges to in different runs of the algorithm
## are parallel to the vector that points roughly towards the mean of the data (data2)."
    
 

print('Code for Question 9:', '\n')   

# Visualisation 
plt.figure(3)
plt.scatter(our_normal_data[:, 0], our_normal_data[:, 1], marker = 'o',  c = 'r')
plt.title('Data cloud for Hebb Rule')
plt.xlabel('u1 (input 1)')
plt.ylabel('u2 (input 2)')

# Creates our random first w value for the third data (our_normal_data with Hebb Rule)
w3 = w_zero 

# Implementing the updating rule to update w for a number of iterations (e.g. 500).
# Hebb rule for updating w

for step in np.arange(0, 500, 1):
    
    plt.figure(3)
    u = our_normal_data[np.remainder(step, our_normal_data.shape[0]), :]
    v = u @ w3
    plt.plot(v, marker='^',  c='b')
    w3 = w3 + delta_t * eta * (v * u)  # Hebb Rule
    plt.plot(v, marker = '^',  c = 'g')
    plt.plot(w3[0], w3[1], marker = '*',  c = 'b')

    
    
plt.show()
    
 
# Answer to Question 9:
## "The vectors found by the Hebb learning rule have the same direction 
## as those found by Oja's rule (on our_normal_data, in Question 7),
## but the length (of w3) grows without bound as a function of the number of iterations.
    
    
    