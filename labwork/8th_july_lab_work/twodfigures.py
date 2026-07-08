import math
#function to calculate area and perimeter of triangle
def triangle_area(base, height):
    return 0.5 * base * height

def triangle_perimeter(a, b, c):
    return a + b + c

#----------------------------------
#function to calculate area and perimeter of circle
def circle_area(radius):
    return math.pi * radius * radius

def circle_circumference(radius):
    return 2 * math.pi * radius


#----------------------------------
#function to crate area and perimeter of square
def square_area(side):
    return side * side

def square_perimeter(side):
    return 4 * side

#----------------------------------
#function to calculate area and perimeter of rectangle
def rectangle_area(length, breadth):
    return length * breadth

def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)