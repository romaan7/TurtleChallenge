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


#Move sequences
moves = 'RRRFFFFRFF'

def rotate():
    global direction
    if direction == 'N':
        direction = 'E'
        return 'East'
    elif direction == 'E':
        direction =  'S'
        return 'South'
    elif direction == 'S':
        direction =  'W'
        return 'West'
    elif direction == 'W':
        direction =  'N'
        return 'North'
    
def move():
    try:
        mine_hit = False
        exit_reached = False
        
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
                return True
        if direction == 'N':
            if map[x-1,y]== '*':
                print('BOOM!')
                return 1
            elif map[x-1,y] == 'e':
                print('Exit Reached')
                return 2        
            else:
                map[x-1,y]='T'
                return True
        if direction == 'S':
            if map[x+1,y]=='*':
                print('BOOM!')
                return 1
            elif map[x+1,y] == 'e':
                print('Exit Reached')
                return 2        
            else:
                map[x+1,y]='T'
                return True
        if direction == 'W':
            if map[x,y-1]=='*':
                print('BOOM!')
                return 1
            elif map[x,y-1] == 'e':
                print('Exit Reached')
                return 2        
            else:
                map[x,y-1]='T'
                return True
    except:
        print('Something went wrong')


def sequence(moves):
    for i in moves:
        if i == 'R':
            print('Rotated '+rotate())
        elif i == 'F':
            if move():
                print( 'Success!')
            elif move()==1:
                print('Mine hit!')
            elif move()==2:
                print('Exit reached')
        else:
            return 'Invalid Move'
            
print(map)
print()
sequence(moves)
print(map)