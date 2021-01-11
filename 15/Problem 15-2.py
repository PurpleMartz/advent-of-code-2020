# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 20:44:05 2021

@author: Marty
"""

data = open("Problem 15 Data.txt", "r").read()
data = data[:-1].split(',')
data = [int(x) for x in data]

# PART 2
# Should take 20-40 seconds
target = 30000000
percentMaxi = target // 50
numMap = dict()
for i in range(len(data)):
    numMap[data[i]] = i

lastNum = data[-2]
currNum = data[-1]
print("Processing... ", end = "", flush = True)
for i in range(len(data) - 1, target):
    numMap[lastNum] = i - 1
    lastNum = currNum
    if lastNum in numMap:
        currNum = i - numMap[lastNum]
    else:
        currNum = 0
    if i % percentMaxi == 0: print('#', end = "", flush = True)
print()

print('PART 2:', lastNum)