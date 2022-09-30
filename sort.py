import math

numList = [1,2,3,4,5]

listOfValues = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)] for m in numList]

for i in listOfValues:
    print(i)

print()
