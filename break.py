i = 1

while  i <= 20:
    if(i % 2) == 0:
        i = i + 1
        continue

    if i == 15:
        break

    print("Odd : ", i)

    i = i + 1
