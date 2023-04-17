# Name: Junhee Youn
# SBUID: 112492955
##################### SCORE ######################
####### Score:  6/10
#################################################
# Remove the ellipses (...) when writing your solutions.
####your output:
# (base) D:\CSE 101 Ass1\Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27>D:/anaconda/python.exe "d:/CSE 101 Ass1/Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27/Junheey/Homework_1.py"
# Traceback (most recent call last):
#   File "d:\CSE 101 Ass1\Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27\Junheey\Homework_1.py", line 27, in <module>
#     print(what_to_wear(celsius))
#   File "d:\CSE 101 Ass1\Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27\Junheey\Homework_1.py", line 15, in what_to_wear
#     if celsius < -10:
# TypeError: '<' not supported between instances of 'function' and 'int'


# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit): 
   celsius = 5/9 * (fahrenheit - 32)
   return celsius

def what_to_wear(celsius):
   if celsius < -10:
       return 'Puffy jacket'
   elif -10 < celsius < 0:
       return 'Scarf'
   elif 0 < celsius < 10:
       return 'Sweater'
   elif 10 < celsius < 20:
       return 'Light jacket'
   else:
       return 'T-shirt'

celsius = fahrenheit2celsius   
print(what_to_wear(celsius))

# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x3, y3)
    area = (abs((x1*y2 + x2*y3 + x3*y1) - (x1*y3 + x2*y1 + x3*y2))/2)
    return area

import math

def euclidean_distance(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance 
    

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    perimeter = s1 +s2 + s3
    return perimeter 
    


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

import math

def deg2rad(deg):
    return (deg * math.pi) / 180
    

def apothem(number_sides, length_side):
   angle = 180 / number_sides
   return length_side / (2* math.tan(angle))
   

def polygon_area(number_sides, length_side):
   return (number_sides * length_side * apothem) / 2




# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

