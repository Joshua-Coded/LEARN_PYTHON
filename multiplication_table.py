import math
import random

# create the multidimensional list

multTable = [[0] * 10 for i in range(10)]

# increment with outer for
for i in range(1, 10):
     for j in range(1, 10):
          multTable[i][j] = i * j

for i in range(1, 10):
     for j in range(1, 10):
           print(multTable[i][j], end=", ")
print()
