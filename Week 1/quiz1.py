# -*- coding: utf-8 -*-
"""
Created on Fri May  8 16:13:47 2020

@author: Dilay Ercelik
"""

# Quiz Week 1   (see also png files)

# Grade: 14/14 (100%)

import numpy as np
import matplotlib.pyplot as plt

#Queston 1

A = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]])

print(A)


#Question 2

#B = A[:, :]        #not the answer
#B = A[1:, [0, 2]]  #not the answer
B = A[[0, 2], 1:]   #the answer
#B = A[[1, 3], 2:]  #not the answer
#B = A[[0, 2], 2:]  #not the answer

print(B) 


#Question 3
##see png document

#Question 4
##see png document

a = np.array([1, 2, 3, 4])

#b = np.ones(5, 5)    # not an answer
#b = a[:2, :2]        # not an answer
b = a[4:]             # an answer
b = np.ones((5, 5))   # an answer
b = np.ones(5,)       # an answer
#b = a[4]             #not an answer
b = a[:5]             # an answer
b = a[:2]             # an answer

print(b)



#Question 5

x = np.random.rand(100)   #the answer
#x = random(100)          #not the answer
#x = np.random(100)       #not the answer

print(x)



#Question 6

#if x > 0.5:              #not the answer
    #x = 1

#[x > 0.5] = 1            #not the answer

#x[> 0.5] = 1             #not the answer

x[x > 0.5] = 1            #the answer

print(x)



#Question 7
x = np.array([1, 2, 3, 4, 5])

#print((x > 1)[:3])                 #not the answer
#print(x[:3] > 1)                   #not the answer
print((x > 1).nonzero()[0][:3])     #the answer
#print(x[x > 1][:3])                #not the answer



#Question 8
#see png document


#Question 9
#see png document



#Question 10
x = np.arange(0, 5, step=0.05)
y = np.sin(x**2)
plt.plot(x,y)
plt.show()

#see png document for answer in the quiz



#Question 11
X = np.array([1,2,3,4,5])

#y = X^3   #not the answer
#y = X.^3  #not the answer
y = X**3   #the answer

print(y)



#Question 12
x = np.array([[1, 2, 3], [2, 3, 4]])
x *= 5
x -= 1
x[x > 10] = 0
x = x.T
print(x)

#see png document for answer



#Question 13

##Option 1            #the answer
#if x in [2, 5, 9]:
   #y = True
#else:
    #y = False

##Option 2            #the answer
#y = False
#if x in [2, 5, 9]:
    #y = True

##Option 3
#y = x in [2, 5, 9]   #the answer

##Option 4
#if x == [2, 5, 9]:
    #y = True
#else:
    #y = False
    
#print(y)



#Question 14
x = np.arange(5)
y = -np.arange(5)
x[y < -2] = 0
import pdb; pdb.set_trace()
x *= 9
print(x)


#see png document for answer












