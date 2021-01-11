# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 12:50:16 2021

@author: Marty
"""

from copy import deepcopy

data = open("Problem 11 Data.txt", "r").read()
data = data[:-1].split('\n')
data = [list(x) for x in data]

def getNewSeat(grid, posI, posJ):
    occupiedCount = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for opI, opJ in directions:
        i = posI
        j = posJ
        while 0 <= i + opI < len(grid) and 0 <= j + opJ < len(grid[0]):
            i = i + opI
            j = j + opJ
            if grid[i][j] == '#':
                occupiedCount += 1
                break
            elif grid[i][j] == 'L':
                break
    if grid[posI][posJ] == 'L' and occupiedCount == 0:
        return '#'
    if grid[posI][posJ] == '#' and occupiedCount >= 5:
        return 'L'
    return grid[posI][posJ]


newData = [[None for _ in range(len(data[0]))] for _ in range(len(data))]
while True:
    # print(data)
    # print()
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            newData[i][j] = getNewSeat(data, i, j)
    if data == newData:
        break
    data = deepcopy(newData)

print("PART 2:", sum(x.count('#') for x in data))