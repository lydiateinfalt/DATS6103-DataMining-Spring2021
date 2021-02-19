
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
print('#', 75 * "-")
print("HW_E.1: Write a script to find duplicates from an array.")
print()
def find_dups (l1, l2):
    l = []
    for item in l1:
        if item in l2:
            l += [item]
    return l


def find_unique (l1, l2):
    l = []
    for item in l1:
        if item not in l2:
            l += [item]
    return l

def main():
    l1 = [1, 2, 'Amir', 19, -3, 'end']
    l2 = [-1, 3.8, "Twilight", 'Would it were so simple', 19]
    # using for loops
    dups = find_dups(l1, l2)
    no_dups = find_unique(l1, l2)
    print('list 1:', l1)
    print('list 2:', l2)
    print()
    print("Using for loops to traverse loops")
    print("list of duplicates ", dups)
    print('list of unique values', no_dups)
    print()
    # using list comprehensions
    l3 = [item for item in l1 if item in l2]
    l4 = [item for item in l1 if not item in l2]
    print("Using list comprehension to compare results with above")
    print("l3 (duplicates): ", l3)
    print("l4 (non-duplicates) list: ", l4)

main()
print('#', 75 * "-")
# =================================================================
# E.2: Write a script that finds all such numbers which are divisible by 2 and 5, less than 1000. If you
# use built in function in python explain the methods and how this methods are working.
# =================================================================
print("HW_E.2: Write a script that finds all such numbers which are divisible by 2 and 5, less than 1000.")
print()
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

for i in range(0, 1000):
    if (i % 2 == 0) and (i % 5 == 0):
        l += [i]
print(l)
print('#', 75 * "-")
# =================================================================
# E.3:
# Write a Python class to convert a roman numeral to an integer. Hint: (Use the following symbols
# and numerals Wiki )
# =================================================================

print("HW_E.3: Write a Python class to convert a roman numeral to an integer.")
print()


class romans_num_int():
    # highest roman numeral this class will convert is 3999
    def int_converter(self, roman):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        nines = {'IX': 9, 'XC': 90, 'CM': 900}
        sum = 0
        l = []
        last = len(roman)
        # print(roman)
        index = last
        pos = 0
        while index > 0:
            key = roman[index - 2] + roman[index - 1]
            # pos represent the tens, hundreds and thousands place
            if pos < 3 and key in nines:
                l += [nines[key]]
                index = index - 2
                pos += 1
            elif roman[index - 1] in roman_dict:
                l += [roman_dict[roman[index - 1]]]
                index = index - 1
        # print(l)

        for item in l:
            sum = sum + item
        return sum


roman_numeral_list = ["MMCDXXI", "XXXIX", "DCCLXXXIX", "MIX", "MDCCLXXVI", "MCMXVIII", "CMXCIX", "MMMCMXCIX", "MCMXCIX"]
my_roman = romans_num_int()
for roman_n in roman_numeral_list:
    print("Roman numeral: ", roman_n + " Integer:", my_roman.int_converter(roman_n))

print('#', 75 * "-")

# =================================================================
# E.4:
# Write a Python class to find sum the three elements of the given array to zero.
# Given: [-20, -10, -6, -4, 3, 4, 7, 10]
# Output : [[-10, 3, 7], [-6, -4, 10]]
# =================================================================
# A simple Python 3 program
# to find three elements whose
# sum is equal to zero

print("HW_E.4: Write a Python class to find sum the three elements of the given array to zero.")
print()

from math import floor

class zero_sum_num:
    def __init__(self, l1):
        self.list = l1
        self.len = len(l1)

    def sum_three(self):
        result = []
        l = sorted(self.list)
        max = self.len

        for i in range(0, max - 2):
            for j in range(i + 1, max - 1):
                for k in range(j + 1, max):
                    if (l[i] + l[j] + l[k] == 0):
                        result.append([l[i], l[j], l[k]])

        return result

list1 = [-20, -10, -6, -4, 3, 4, 7, 10, 8, 12, 4]
my_list = zero_sum_num(list1)
print("Input list", list1)
print("Output", my_list.sum_three())
print('#', 75 * "-")


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
print("HW_E.5: Answer all the class exercise questions (Lecture 3)")
print("Class_Ex1: Write a python script (use lass) to simulate a Stopwatch.")
print()
import time

class stopwatch:
    def __init__(self):
        self.reset()

    def start(self):
        self.start_time = time.perf_counter()
        # print(self.start_time)

    def stop(self):
        self.end_time = time.perf_counter()
        # print(self.end_time)
        self.elapsed_time += self.end_time - self.start_time
        # print("Time Elapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))

    def reset(self):
        self.start_time = 0.0
        self.end_time = 0.0
        self.elapsed_time = 0.0

class stopwatch_counter(stopwatch):

    def start(self):
        super(stopwatch_counter, self).start()

    def stop(self):
        super(stopwatch_counter, self).stop()

from time import sleep
timer = stopwatch_counter()
count = 0
timer.start()
count +=1
sleep(10)
timer.stop()
print("Time: ", timer.elapsed_time, "Count: ", count)
timer.start()
count +=1
sleep(5)
timer.stop()
print("Time: ", timer.elapsed_time, "Count: ", count)
timer.start()
count +=1
sleep(10)
timer.stop()
print("Time: ", timer.elapsed_time, "Count: ", count)
print('#', 75 * "-")

# =================================================================
# Class_Ex2:
# Write a python script (use class)to implement pow(x, n).
# ----------------------------------------------------------------

print("Class_Ex2: Write a python script (use class)to implement pow(x, n).")

from math import pi

class power():
    def __init__(self,base, exp):
        self.base = base
        self.exponent = exp
        self.answer = self.base ** self.exponent

    def display(self):
        return self.answer

print(power(2,1).display())




print('#', 75 * "-")

# =================================================================
# Class_Ex3:
# Write a python class to calculate the area of rectangle by length
# and width and a method which will compute the area of a rectangle.
# ----------------------------------------------------------------


print("Class_Ex3: Write a python class to calculate the area of rectangle by length "
      "and width and a method which will compute the area of a rectangle.")

class rectangle():

    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width

my_rectangle = rectangle(15, 4)
print("Rectangle dimensions: ", my_rectangle.length, "x", my_rectangle.width)
print("Area is", my_rectangle.area(), "in square units.")
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

from math import pi

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 4 * pi * pow(self.radius, 2)

    def perimeter(self):
        return 2 * pi * self.radius

r = float(input("Enter radius of a circle: "))
my_circle = circle(r)
print("Circle's area", my_circle.area(), "in square units.")
print("Circle's perimeter", my_circle.perimeter(), "in unit.")


print('#', 75 * "-")
