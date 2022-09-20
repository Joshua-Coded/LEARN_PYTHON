#we'll provide different output based on age
#1 - 18 -> Important
# 21, 50, 65 ->  important
#All others -> Not important
#Receive age amd store in age
age = eval(input("Enter age: "))

# and : if both condition are true it return true
# or : if either condition  is true then retun true
#not  :
#if age is both greater than or equals to 1 and less than or equals  to 18 important

if (age >= 1) and (age <= 18):
    print("Important Birthday")

#if age is either 21 or 50 important
elif (age == 21) or (age == 50):
    print("Important Birthday")
# we check if age is less than 65 and then convert true to false and vice versa
elif not(age < 65):
    print("Important birthday")

# else not important
else:
    print("sorry Not Important")
