# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 18:55:42 2020

@author: Sewcary
"""


import numpy as np 

np.ndarray([1,5,3])

l = ['Fara','Jean','Por','Noe','Pat']
m = ['Rox','ROu','teo','Phil']

print(l)

l.extend(m)

l.insert(1,'MOI')

print (l)

l.remove('MOI')

print(l.index('Phil'))

l.count('ROu')

l.sort()

print (l)

l.sort(reverse = True)
print(l)
string ="La chaine est à l'endroit"

print(string[::-1])

l = np.zeros((4,2))

print(l) 

l= np.random.randn(4,3)
print(l)      

l = np.random.randint(1,10,100)
print(l)    

l = np.linspace(1,10,20)
print(l)      
l= np.arange(1,12,1)
print(l)      
     