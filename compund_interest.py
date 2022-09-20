#have the users enter their investment amount and expected interest
# each year their investment will increase bt their investment + their investment * interest rate is
# print out the earnings after a 10 year period

# ask for the money invested + the interest rate

money = input("how much to invest: ")
interest_rate = input("Interest Rate: ")

# convert the value to a float
money = float(money)

# convert value to a float and round the percentage rate by 2 digits
interest_rate = float(interest_rate) * .01
#cycle through  10 years using a for loop and range from 0 to 9
for i in range(10):
    money = money + (money * interest_rate)
#output the results
print("Investment after 10 years:  {:.2f}".format(money))
    
