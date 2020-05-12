# -*- coding: utf-8 -*-
"""
Created on Tue May 12 14:26:22 2020

@author: Dilay Ercelik
"""

# Quiz 4
from math import log2



# Question 1
print('Question 1:', '\n')

# Using the generalised formula for the entropy (see supplementary tutorial notes)
# calculated in bits, i.e. using the base 2 logarithm log2
H_of_F = (- 0.1 * log2(0.1)) + (- 0.9 * log2(0.9))

print('The entropy of the described Bernoulli distribution F is H(F) = {}'.format(H_of_F))


# Question 2 (continued from Question 1)
print('Question 2:', '\n')

# Using formula for th mutual information MI:
# MI(S,F)= total entropy - average noise entropy total entropy
# total entropy = H(S) or H(F): we already know H(F)

MI_S_F = H_of_F - ((0.1) * (1/2) * log2(1/2) + (0.1) * (1/2) * log2(1/2) + (0.9) * (1/18) * log2(1/18) + (0.9) * (17/18) * log2(17/18))

print('The mutual information MI(S,F) is equal to {}'.format(MI_S_F))