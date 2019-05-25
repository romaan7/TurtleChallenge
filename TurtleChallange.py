# -*- coding: utf-8 -*-
"""
Created on Sat May 25 14:55:45 2019

@author: shaikhr
"""

import numpy as np

#initial game setting

#Map dimension
n,m = 4,5
map = np.zeros([n,m], dtype=object)

#T position and direction
x,y = 0,0
direction = 'S'
map[x,y]='T'

#Mines position
map[1,1]='*'
map[1,3]='*'
map[3,3]='*'

#Exit position
map[2,4]='*'
def rotate():
    global direction
    if direction == 'N':
        direction = 'E'
    elif direction == 'E':
        direction =  'S'
    elif direction == 'S':
        direction =  'W'
    elif direction == 'W':
        direction =  'N'
    
def move():
    result = np.where(map == 'T')
    listOfCoordinates= list(zip(result[0], result[1]))
    x = listOfCoordinates[0][0]
    y = listOfCoordinates[0][1]
    map[listOfCoordinates[0]] = 0
        
    if direction == 'E':
        if map[x,y+1] == '*':
            print('BOOM!')
            return 1
        elif map[x,y+1] == 'e':
            print('Exit Reached')
            return 2
        else:
            map[x,y+1]='T'
    if direction == 'N':
        if map[x-1,y]== '*':
            print('BOOM!')
            return 1
        elif map[x-1,y] == 'e':
            print('Exit Reached')
            return 2        
        else:
            map[x-1,y]='T'
    if direction == 'S':
        if map[x+1,y]=='*':
            print('BOOM!')
            return 1
        elif map[x+1,y] == 'e':
            print('Exit Reached')
            return 2        
        else:
            map[x+1,y]='T'
    if direction == 'W':
        if map[x,y-1]=='*':
            print('BOOM!')
            return 1
        elif map[x,y-1] == 'e':
            print('Exit Reached')
            return 2        
        else:
            map[x,y-1]='T'


print(map)
print()
rotate()
rotate()
rotate()
move()
move()
move()
move()
rotate()
move()
move()
move()


print(map)