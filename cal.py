num1, operator, num2 = input("Enter calculation ").split()

#convert string to int

num1 = int(num1)
num2 =int(num2)

#operation

if operator == "+":
    print("{} + {} = {}".format(num1, num1, num1 + num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num1, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num1, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num1, num1 / num2))
else:
    print("Enter either + * / - operation")
