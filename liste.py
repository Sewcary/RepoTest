# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 20:50:34 2020

@author: Sewcary
"""
friends2 = {'Robert','Paris','North','Kanye'}
friends = ['Kevin','Jimmy' ,"Karen","Jim","Oscar","Tommy"] 
print(friends) 

print (friends[1::])

friends.extend(friends2) 

print (friends)

friends.insert(0,'Fara')

print(friends)

friends.remove('Fara')

print(friends)


print (friends)

print (friends.index("Robert"))
print(friends.count('North'))

friends.sort(reverse =True )

print(friends)

friends2 = friends.copy()
print(friends2)

friends.reverse()

print(friends)

phrase  = "Phrase de test numero"

print(phrase[::-1])
print(phrase)