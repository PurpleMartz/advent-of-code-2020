# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 22:33:32 2021

@author: Marty
"""

data = open("Problem 12 Data.txt", "r").read()
data = data[:-1].split('\n')

# PART 2
faces = {'W': (-1, 0), 'N': (0, 1), 'E': (1, 0), 'S': (0, -1)}
faceKeys = list(faces.keys())
location = [0, 0]
waypoint = [10, 1] # relative distance from the ship

def rotate90(x, y, clockwise):
    coeff = 1 if clockwise else -1
    return coeff * y, coeff * -x

def rotate90Multiple(times, x, y, clockwise):
    if times == 0:
        return x, y
    x, y = rotate90(x, y, clockwise)
    return rotate90Multiple(times - 1, x, y, clockwise)

for instruction in data:
    direction = instruction[:1]
    units = int(instruction[1:])
    if direction in faceKeys:
        waypoint[0] += (faces[direction][0] * units)
        waypoint[1] += (faces[direction][1] * units)
    elif direction == 'F':
        location[0] += (waypoint[0] * units)
        location[1] += (waypoint[1] * units)
    else:
        units = int(units / 90)
        if direction == 'L':
            waypoint = list(rotate90Multiple(units, *waypoint, False))
        elif direction == 'R':
            waypoint = list(rotate90Multiple(units, *waypoint, True))
        else:
            raise Exception("Unkown instruction!")
            
print("PART 2:", abs(location[0]) + abs(location[1]))