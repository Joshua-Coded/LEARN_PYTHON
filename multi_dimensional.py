import random

import math

listTable = [[0] * 10 for i in range(10)]

for i in range(10):
    for j in range(10):
        listTable[i][j] = "%d : %d" %(i, j)


for i in range(10):
    for j in range(10):
        print(listTable[i][j], end=" || ")
        
