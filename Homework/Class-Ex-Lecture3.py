
# Lydia Teinfalt
# DATS 6103: Data Mining
# Spring 2021
# 02/01/2021
# Lecture 3 Exercises
# =========================
# =================================================================
# Class_Ex1:
# Writes a python script (use class) to simulate a Stopwatch .
# push a button to start the clock (call the start method), push a button
# to stop the clock (call the stop method), and then read the elapsed time
# (use the result of the elapsed method).
# ----------------------------------------------------------------
import math
from math import pi

print("Class_Ex1: Write a python script (use lass) to simulate a Stopwatch.")

import time


def start():
    start = time.time()
    return start


def stop():
    end = time.time()
    return end


def convert_time(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Elapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))


input("Push Enter button to start the stopwatch.")
start_t = start()

input("Press Enter button stop the stopwatch.")
end_t = stop()
print("Start ", start_t)
print("Stop ", end_t)
print(convert_time(end_t - start_t))

print('#', 75 * "-")

# =================================================================
# Class_Ex2:
# Write a python script (use class)to implement pow(x, n).
# ----------------------------------------------------------------
print("Class_Ex2: Write a python script (use class)to implement pow(x, n).")


def main():
    # ask user to enter radius
    r = float(input("Enter radius of a sphere: "))
    volume = 4.0 / 3.0 * pi * pow(r, 3)
    area = 4 * pi * pow(r, 2)
    print("Sphere volume is ", volume, "in cubic units.")
    print("Sphere area", area, "in square units.")


main()

print('#', 75 * "-")

# =================================================================
# Class_Ex3:
# Write a python class to calculate the area of rectangle by length
# and width and a method which will compute the area of a rectangle.
# ----------------------------------------------------------------
print("Class_Ex3: Write a python class to calculate the area of rectangle by length "
      "and width and a method which will compute the area of a rectangle.")


def main():
    # ask user to enter length and
    l = float(input("Enter rectangle's length: "))
    w = float(input("Enter rectangle's width: "))
    area = l * w
    print("Sphere area", area, "in square units.")


main()

print('#', 75 * "-")

# =================================================================
# Class_Ex4:
# Write a python class and name it Circle to calculate the area of circle
# by a radius and two methods which will compute the area and the perimeter
# of a circle.
# ----------------------------------------------------------------
print("Class_Ex4: Write a python class and name it Circle to calculate the area of circle"
      "by a radius and two methods which will compute the area and the perimeter"
      "of a circle.")


class circle:
    '''
    Circle class calculates area and perimeter of a circle by asking user to input radius.
    '''
    import math
    # ask user to enter radius
    r = float(input("Enter radius of a circle: "))
    area = 4 * math.pi * pow(r, 2)
    perimeter = 2 * math.pi * r
    print("Circle's area", area, "in square units.")
    print("Circle's perimeter", perimeter, "in unit.")

circle
# print(help(circle))
print('#', 75 * "-")
