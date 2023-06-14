'''
Author: Ashton Hogge

Comment: Practicing using variables in coding

'''

import math

square = input("What is the length of a side of the square? ")
squarea = float(square) ** 2
print(f"The area of the square in centimeters is: {squarea: .1f}, in square meters: {squarea / 10000: .6f} \n")

cube_area = int(square) ** 3
print(f"The volume of the cube is: {cube_area: .3f}\n")

rect_length = input ("What is the length of the rectangle? ")
rect_width = input ("What is the width of the rectangle? ")
rectangle_area = int(rect_length) * int(rect_width)
print(f"The area of the rectangle is: {rectangle_area: .2f}\n")

circle_radius = int(input ("What is the radius of the circle? "))
circle_area = math.pi * circle_radius ** 2
print(f"The area of the circle is: {circle_area: .2f}\n")

volume_sphere = 4/3 * math.pi * circle_radius ** 3
print(f"The volume of the sphere is: {volume_sphere: .3f}\n")
