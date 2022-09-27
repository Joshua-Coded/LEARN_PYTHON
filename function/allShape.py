import math

def get_area(shape):
    shape = shape.lower()


    if shape == "rectange":
        rectangle_area()
        
    elif shape == "circle":
        circle_area()
    else:
        print("please enter rectangle, or circle")


def rectangle_area():
    length = float(input("Enter the lenght :"))
    width = float(input("Enter the width :"))

    area = lenght * width

    print("the area of rectangle is", area)


def circle_area():
    radius = float(input("Enter the radius "))

    area = math.pi * (math.pow(radius, 2))
    print("the area of our circle is {:.2f}".format(area))

    
def main():
    shape_type = input("Get area for what shape: ")

    get_area(shape_type)
    

main()
