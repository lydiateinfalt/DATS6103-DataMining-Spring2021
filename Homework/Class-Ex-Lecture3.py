
# Lydia Teinfalt
# DATS 6103: Data Mining
# Spring 2021
# 02/01/2021
# Homework 3 and Lecture 3 Exercises
# =========================

# =================================================================
# E.1:
# Write a script to find duplicates from an array (define an array with some duplicates on it). If
# you use built in function in python explain the methods and how this methods are working.
# =================================================================
"""
def find_dups (l1, l2):
    l3 = []
    for item in l1:
        if item in l2:
            l3 += [item]
    return l2


def find_unique (l1, l2):
    l3 = []
    for item in l1:
        if item not in l2:
            l3 += [item]
    return l3

def main():
    l1 = [1, 2, 'Amir', 19, -3, 'end']
    l2 = [-1, 3.8, "Twilight", 'Would it were so simple', 19]
    dups = find_dups(l1, l2)
    no_dups = find_unique(l1, l2)
    print('list 1', l1)
    print('list 2', l2)
    print("list of duplicates ", dups)
    print('list of unique values', no_dups)
    l3 = [item for item in l1 if item in l2]
    l4 = [item for item in l1 if not item in l2]
    print("l3", l3)
    print("l4", l4)

main()
"""
# =================================================================
# E.2: Write a script that finds all such numbers which are divisible by 2 and 5, less than 1000. If you
# use built in function in python explain the methods and how this methods are working.
# =================================================================
"""
def div_2(n):
    if n%2 == 0:
        return True
    else:
        return False

def div_5(n):
    if n%5 == 0:
        return True
    else:
        return False
l = []
for i in range (0,1000):
    if div_2(i) and div_5(i):
        l += [i]
print(l)
"""
# =================================================================
# E.3:
# Write a Python class to convert a roman numeral to an integer. Hint: (Use the following symbols
# and numerals Wiki )
# =================================================================
class romans_num_int():
    def int_converter(self, roman):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        nines = {'IX': 9, 'XC': 90, 'CM': 900}
        sum = 0
        l = []
        last = len(roman)
        print(roman)
        index = last
        pos = 0
        while index > 0 :
            key = roman[index - 2] + roman[index - 1]
            if pos < 3 and key in nines:
                l += [nines[key]]
                index = index - 2
                pos += 1
            elif roman[index-1] in roman_dict:
                l += [roman_dict[roman[index-1]]]
                index = index - 1
        print(l)

        for item in l:
            sum = sum + item
        return sum

print(romans_num_int().int_converter("MMCDXXI"))
print(romans_num_int().int_converter("XXXIX"))
print(romans_num_int().int_converter("DCCLXXXIX"))
print(romans_num_int().int_converter("MIX"))
print(romans_num_int().int_converter("MDCCLXXVI"))
print(romans_num_int().int_converter("MCMXVIII"))
print(romans_num_int().int_converter("CMXCIX"))
print(romans_num_int().int_converter("MMMCMXCIX"))







# =================================================================
# E.4:
# Write a Python class to find sum the three elements of the given array to zero.
# Given: [-20, -10, -6, -4, 3, 4, 7, 10]
# Output : [[-10, 3, 7], [-6, -4, 10]]
# =================================================================


# =================================================================
# E.5:
# Answer all the class exercise questions (Lecture 3) and submit it (Check the instructions).

# =================================================================
# Class_Ex1:
# Writes a python script (use class) to simulate a Stopwatch .
# push a button to start the clock (call the start method), push a button
# to stop the clock (call the stop method), and then read the elapsed time
# (use the result of the elapsed method).
# ----------------------------------------------------------------
import math
from math import pi
"""
print("Class_Ex1: Write a python script (use lass) to simulate a Stopwatch.")
import time

class stopwatch:
    def __init__(self):
        time.clock()

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


s = stopwatch
input("Push Enter button to start the stopwatch.")
start_t = s.start()

input("Press Enter button stop the stopwatch.")
end_t = s.stop()
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
"""