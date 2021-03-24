# Lydia Teinfalt
# DATS 6103: Data Mining
# Spring 2021
# 02/01/2021
# Homework 2 Exercises
# Write a function called is_sorted that takes a list as a parameter and returns True
# if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that
# the elements of the list can be compared with the relational operators <, >, etc.
# For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should return
# False.
def is_sorted(l):
    l1= []
    l1 = sorted(l)
    if l == l1:
        return True
    else:
        return False
#
my_list = [1,2,2]
my_list = ['b','a']
if is_sorted(my_list):
    print("List 1", my_list, " is sorted")
else:
    print("List 1", my_list, " is not sorted")
# #
# Exercise 10.7. Two words are anagrams if you can rearrange the letters from one to spell the other.
# Write a function called is_anagram that takes two strings and returns True if they are anagrams.
# #
def is_anagram(l1, l2):
    print(l1[::-1])
    if l2 == l1[::-1]:
        print("True")
    else:
        print("False")
#
print(is_anagram('realtor', 'rotlaer'))
print(is_anagram('hydro', 'ordyh'))
#
def has_duplicates(list1):
    if len(list1) == len(set(list1)):
        return False
    else:
        return True

print(has_duplicates([1, 2, 'Amir', 19, -3, 'Amir', 'end']))
# Ask the user for a number.
# Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
# #
# Extras:
#
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers:
# one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
#
def odd_even(num):
    attr = ""
    if num % 4 == 0:
        attr = "multiple4"
    elif num % 2 == 0:
        attr = "even"
    else:
        attr = "odd"
    return attr
#
num = eval(input("Please enter a number: "))
result = odd_even(num)
if result == "even":
    print("Number is even")
elif result == "multiple4":
    print("Number is a multiple of 4")
else:
    print("Number is odd")
#
####
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [x for x in a if x < 10]
print(b)
#
num = int(input("Please choose a number to divide: "))
list1= []
listRange = list(range(1,num+1))
for x in listRange:
     if num % x == 0:
         list1.append(x)
#
print(list1)
#
#

import os
#change directory
os.chdir("C:/Users/teinfalt/Data-Mining")
print("Operating System: ", os.name)

#current working directory
cwd = os.getcwd()
directories = os.listdir(cwd)
dirs = []
files1 = []

#get list of files and directories
for item in directories:
    if os.path.isdir(item):
        dirs += [item]

    else:
        files1 += [item]
        # print("File name", item)
#write to a file
fout = open('output.txt', 'w')
line1 = "List of directories,\n"
fout.write(line1)
line2 = "List of files.\n"
fout.write(line2)
fout.write(str(files1))
fout.close()
print('#', 50 * "-")


class Line:

    # create two coordinates as attributes
    def __init__(self, coor1, coor2):
        self.xy1 = coor1
        self.xy2 = coor2

    def distance(self):
        x1, y1 = self.xy1
        x2, y2 = self.xy2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def slope(self):
        x1, y1 = self.xy1
        x2, y2 = self.xy2
        return (y2 - y1) / (x2 - x1)
# Example Output
coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print('#', 50 * "-")

import matplotlib.path as mpath
shape_description = [
( 1., 2., mpath.Path.MOVETO),
( 1., 1., mpath.Path.LINETO),
( 2., 1., mpath.Path.LINETO),
( 2., -1., mpath.Path.LINETO),
( 1., -1., mpath.Path.LINETO),
( 1., -2., mpath.Path.LINETO),
(-1., -2., mpath.Path.LINETO),
(-1., -1., mpath.Path.LINETO),
(-2., -1., mpath.Path.LINETO),
(-2., 1., mpath.Path.LINETO),
(-1., 1., mpath.Path.LINETO),
(-1., 2., mpath.Path.LINETO),
( 0., 0., mpath.Path.CLOSEPOLY),
]
import numpy as np

u, v, codes = zip(*shape_description)
my_marker = mpath.Path(np.asarray((u, v)).T, codes)

import matplotlib.pyplot as plt

data = np.random.rand(10, 10)
plt.scatter(data[:,0], data[:, 1], c = 'b', marker = my_marker, s = 120)
plt.show()
# bowtie shape
shape_description1 = [
( 0., 0., mpath.Path.MOVETO),
( 0., 2., mpath.Path.LINETO),
( 1., 1., mpath.Path.LINETO),
( 2., 2., mpath.Path.LINETO),
( 2., 0., mpath.Path.LINETO),
( 1., 1., mpath.Path.LINETO),
( 0., 0., mpath.Path.CLOSEPOLY),
]
#scatter plot with bow-tie shapes
x, y, codes1 = zip(*shape_description1)
my_marker1 = mpath.Path(np.asarray((x, y)).T, codes1)
plt.scatter(data[:,0], data[:, 1], c = 'b', marker = my_marker1, s = 120)
plt.show()

#mathplotlib graph of a bow-tie
from numpy import *
from matplotlib.pyplot import *

x=([0,0,1,2,2,1,0])
y = ([0, 2, 1, 2, 0, 1,0])
plot(x,y)
show()

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as pat

fig, ax = plt.subplots()

#create simple line plot
ax.hlines(4,0,3)
plt.vlines(8, 2, 4)
ax.hlines(4,7,10)
ax.hlines(2,8,10)
ax.hlines(4,14,20)
ax.hlines(2,14,20)
plt.vlines(8, 2, 4)
plt.vlines(20, 2, 2.2)
plt.vlines(20, 3.7, 4)
#add rectangle to plot
ax.add_patch(Rectangle((3, 3),4,1.5))
ax.add_patch(Rectangle((10, 3),4, 1.5))
ax.add_patch(Rectangle((10, 1),4, 1.5))
ax.add_patch(Rectangle((18, 2.2),4, 1.5))

#display plot
plt.show()