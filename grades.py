# if age is 5 go to kindergarten
# ages 6 through 17 goes to grades 1 through 12
#if age is grater than 17 say go to college
#try to complete with 10 or less lines

# ask got age

age = eval(input("enter age"))
#handle id age < 5
if age < 5:
    print("too young for school")
# special output just for age 5
elif age == 5:
    print("Go to kindergarten")

# since a number is the result for ages 6-17 we can check them all with 1 condition
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("go to {} grade".format(grade))

# handle
else:
    print("go to college")
