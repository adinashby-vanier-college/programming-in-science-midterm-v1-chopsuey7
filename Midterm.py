import math
from math import *
# Q1: Calculate the area of a circle

def area_of_circle(radius):
    area= pi * (radius) ** 2
    return round(area , 2)


# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    if n >= 4:
        result= ["*"]
        spaces= 1
        for i in range(0 , n-2):
            result.append("*" + " " * (space * (i)) + "*")
        result.append(n * "*")
        return "\n".join(result0).rstrip()
    else:
        return "The triangle height should be at least 4."

# Q3: Inverted Pyramid
def inverted_pyramid(n):
    if n>=3:
        result= []
        spaces=(n - 1)
        end= [" " * spaces + "*"]
        ispace= -1
        for i in range (n + (n-1), 1, -2):
            ispace+= 1
            result.append(" " * ispace + "*" * i)
        return "\n".join(result + end).rstrip()

    else:
        return "The pyramid height should be at least 3."

    

# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()