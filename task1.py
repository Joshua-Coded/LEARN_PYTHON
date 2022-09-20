num1, num2 = input("Enter 2 numbers: ").split()

num1 = int(num1)
num2 = int(num2)

sum = num1 + num2
diff = num1 - num2
div = num1 / num2
mul = num1 * num2
mol = num1 % num2

print("{} + {} = {}".format(num1, num2, sum ))
print("{} - {} = {}".format(num1, num2, diff ))
print("{} / {} = {}".format(num1, num2, div ))
print("{} * {} = {}".format(num1, num2, mul ))
print("{} % {} = {}".format(num1, num2, mol))
