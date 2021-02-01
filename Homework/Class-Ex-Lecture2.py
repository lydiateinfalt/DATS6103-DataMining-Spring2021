# Lydia Teinfalt
# DATS 6103: Data Mining
# Spring 2021
# 02/01/2021
# Lecture 2 Exercises
# =================================================================
# Class_Ex1:
# Write a program that simulates the rolling of a die.
# ----------------------------------------------------------------
import random
print("Class_Ex1:")

die = random.randrange(1, 7)
print(die)

print("+--------+")
empty = '|        |'
middle = '|   *    |'
left = '|*       |'
right = '|       *|'
half_left = '|*   '
half_right = '   *|'
if die == 1:
    print(empty)
    print(empty)
    print(middle)
    print(empty)
    print(empty)
if die == 2:
    print(left)
    print(empty)
    print(empty)
    print(empty)
    print(right)
if die == 3:
    print(left)
    print(empty)
    print(middle)
    print(empty)
    print(right)
if die == 4:
    print(half_left + half_right)
    print(empty)
    print(empty)
    print(empty)
    print(half_left + half_right)
if die == 5:
    print(half_left + half_right)
    print(empty)
    print(middle)
    print(empty)
    print(half_left + half_right)
if die == 6:
    print(half_left + half_right)
    print(empty)
    print(half_left + half_right)
    print(empty)
    print(half_left + half_right)
print("+--------+")
print()
print('#', 75*"-")

# =================================================================
# Class_Ex2:
# Answer  Ex1 by using functions.
# Write function within function
# ----------------------------------------------------------------
print("Class_Ex2: Answer Ex1 by using functions. Write function within function.")
from random import randrange
def roll():
    return randrange(1,7)

def display_die(n):
    print(n)
    print("+--------+")
    empty = '|        |'
    middle = '|   *    |'
    left = '|*       |'
    right = '|       *|'
    half_left = '|*   '
    half_right = '   *|'
    if n == 1:
        print(empty)
        print(empty)
        print(middle)
        print(empty)
        print(empty)
    if n == 2:
        print(left)
        print(empty)
        print(empty)
        print(empty)
        print(right)
    if n == 3:
        print(left)
        print(empty)
        print(middle)
        print(empty)
        print(right)
    if n == 4:
        print(half_left + half_right)
        print(empty)
        print(empty)
        print(empty)
        print(half_left + half_right)

    if n == 5:
        print(half_left + half_right)
        print(empty)
        print(middle)
        print(empty)
        print(half_left + half_right)

    if n == 6:
        print(half_left + half_right)
        print(empty)
        print(half_left + half_right)
        print(empty)
        print(half_left + half_right)
    print("+--------+")

def main():
    print("This program rolls the die 3x to demonstrate randomness.")
    for i in range(0,3):
        display_die(roll())

main()
print()
print('#', 75*"-")
# =================================================================
# Class_Ex3: 
# Randomly Permuting a List
# ----------------------------------------------------------------
print("Class_Ex3: Randomly permuting a List. ")

def random_permute(a):
    import random
    new_list= a[:]
    random.shuffle(new_list)
    return new_list


original_list = [1, 8, 99, 17]
print("Original list: ", original_list)
print("Randomly permuted list: ", random_permute(original_list))
print()
print('#', 75*"-")

# =================================================================
# Class_Ex4:
# Write a program to convert a tuple to a string.
# ----------------------------------------------------------------
print("Class_Ex4: Write a program to convert a tuple to a string.")
t = tuple("Monsieur Lupin")
print("Tuple: ", t)
print("String: ",''.join(t))
print('#', 75*"-")

# =================================================================
# Class_Ex5:
# Write a program to get the 3th element of a tuple.
# ----------------------------------------------------------------
print("# Class_Ex5:  Write a program to get the 3th element of a tuple.")
t = tuple("lupins")
# Python counts start with 0 so the 3th element would be 2.
print("Tuple: ", t)
print("Tuple's 3th element: ", t[2])
print('#', 75*"-")

# =================================================================
# Class_Ex6:
# Write a program to check if an element exists in a tuple or not.
# ----------------------------------------------------------------
print("Class_Ex6: Write a program to check if an element exists in a tuple or not.")
t = tuple("apocalypse")
n = "a" # example of element that exists
# n = 1
if n in t:
    print("Yes, element", n, "is in tuple", t)
else:
    print("No, element", n, "is not in tuple", t)
print('#', 75*"-")

# =================================================================
# Class_Ex7:
# Write a program to check a list is empty or not.
# ----------------------------------------------------------------
print("Class_Ex7: Write a program to check a list is empty or not.")
mylist = ['a', 8.9, 99, [10,20]]
# mylist = [1, 2, 'Amir', 19, -3, 'end']
# mylist = []

if not mylist:
    print("List is empty")
else:
    print("List is not empty = ", mylist)

print('#', 75*"-")

# =================================================================
# Class_Ex8:
# Write a program to generate a 4*5*3 3D array that each element is O.
# ----------------------------------------------------------------
print("Class_Ex8: Write a program to generate 4*5*3 3D array that each element is 0.")
my_3D_array = []
x=4
y=5
z=3
for i in range(x):
    my_3D_array.append([])
    for j in range(y):
        my_3D_array[i].append([])
        for k in range(z):
            my_3D_array[i][j].append([0])

print("The 4*5*3 3D array that each element is O", my_3D_array)
print('#', 75*"-")
