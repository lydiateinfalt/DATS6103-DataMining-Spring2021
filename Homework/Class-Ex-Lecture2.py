# Lydia Teinfalt
# DATS 6103: Data Mining
# Spring 2021
# 02/01/2021
# Lydia Teinfalt
# DATS 6103: Data Mining
# Spring 2021
# 02/01/2021
# Homework 2 Exercises
# =================================================================
# E.1:
# Here is a search algorithm for arrays. The inputs are the array, which we call array; the number
# n of elements in array; and target, the number being searched for. The output is the index in
# array of target:
#   1. Let min = 0 and max = n-1.
#   2. Compute guess as the average of max and min, rounded down (so that it is an integer).
#   3. If array[guess] equals target, then stop. You found it! Return guess.
#   4. If the guess was too low, that is, array[guess] ¡ target, then set min = guess + 1.
#   5. Otherwise, the guess was too high. Set max = guess - 1.
#   6. Go back to step 2.
# i. Convert the following algorithm to a proper code and explain the process of the search.
# ii. What are the pro and cons of this method?
# ----------------------------------------------------------------
print('#',75*"-")
print("Homework_E.1: Implement search algorithm based on pseudo code.")
import math

def guess_calc(min, max):
    '''

    :param min: lowest number
    :param max: highest number
    :return: returns average of max and min, rounded down (
    '''
    guess_float = float((min + max) / 2)
    guess = int(math.floor(guess_float))
    return guess

def search(array, n, target):
    min = 0
    max = n - 1
    guess = guess_calc(min, max)
    while guess in range(0, n):
        if array[guess] == target:
            return guess
        elif array[guess] < target:
            min = guess + 1
        else:
            max = guess - 1
        guess = guess_calc(min, max)
    return guess

def main():
    # l is the array input

    # example of a list where the algorithm will work
    l = [11, 22, 33, 44, 55]

    # example of a list where the algorithm will not work
    # l = [99, 88, 77, 66, 55, 44, 22]
    # l = [5, 22, 1, 33]
    # l =[99, 88, 77, 22]
    # n number of elements in th array
    n = len(l)
    # target is the number being searched for in the array
    target = 22
    # index in array l matching target
    index = int(search(l, n, target))
    print("List: ", l)
    print("Target: ", target)
    if index >= 0 and index <= n:
        print("Index: ", index)
        print("List[n] ", l[index])
    else:
        print("Target not found due to logical error")

print()
main()

print("The algorithm is not correct as is currently stated in the pseudo code. Using the criteria array[guess] < target")
print("to compare values in a list when the values not in order is flawed logic.")
print("It assumes that the array is sorted in ascending order in order the algorithm to work.")
print("If the array is sorted, it would be an efficient algorithm to search for a value in an array.")
print('#', 75*"-")

# =================================================================
# E.2:
# Work on a script to count the number of characters or (frequency) in a string.
# =================================================================
print("Homework_E.2: Work on a script to count the number of characters or (frequency) in a string.")

def main():
    '''

    :return: Returns a dictionary in no order of display the number of times a character appears in the sample string
    '''
    # Sample string
    input_string = "Documentsinabriefcasesssd"
    print("Sample string", input_string)

    # instantiate a new dictionary d1
    d1 = dict()
    count = 0

    for index in input_string:
        if index not in d1:
            d1[index] = 1
        else:
            d1[index] += 1
    print(d1)

main()

print('#', 75*"-")
# =================================================================
# E.3:
# Write a function that takes a list of words and returns the length of the longest one.
# =================================================================
print("Homework_E.3: Write a function that takes a list of words and returns the length of the longest one.")

def find_longest_word(l1):
    '''
    :param l1:
    :return:
    the length of the longest word from list l1
    '''
    n = len(l1)
    temp_len = 0
    max_len = 0
    for i in range(0, n):
        temp_len = len(l1[i])
        if temp_len > max_len:
            max_len = temp_len
    return max_len

def main():
    # Sample list l
    l = ["Unless", "you're", "Python", "unanimous"]

    # calls method find_longest_word and passes in the sample list l
    longest = find_longest_word(l)
    print("List", l)
    print("Longest word length", longest)

main()
print('#', 75*"-")

# =================================================================
# E.4:
# Make up your own list and work on a program to get the smallest number from the list.
# =================================================================
print("Homework_E.4: Make up your own list and work on a program to get the smallest number from the list.")


def main():
    '''
    Program returns the smallest number from a list.
    '''
    l_num = [-101, 99,1,45,3,8, 50, -1, -100]
    num = l_num[0]

    for i in range(0, len(l_num)):
        if l_num[i] <= num:
            num = l_num[i]

    # loop through to find smallest number instead of sort
    print("List", l_num)
    print("Smallest number from the list", num)

main()

print('#', 75*"-")
# =================================================================
# E.5:
# Work on a function that takes two lists and returns same (or True) if they have at least one
# common element.
# =================================================================
print("Homework_E.5: Work on a function that takes two lists and returns same (or True) if they have at least one.")

def element_in_common(l1, l2):
    '''
    Function that takes two lists and returns same (or True) if they have at least one.
    '''
    m = len(l1)
    n = len(l2)
    for i in range (0, m):
        if l1[i] in l2:
            return True
        test = False
    return test

def main():
    test_list1 = [1, 4, 77, -3, "Amir"]
    test_list2 = [2, 5, 66, "Amir", 0]
    print("List 1", test_list1)
    print("List 2", test_list2)
    if element_in_common(test_list1, test_list2):
        print("Yes, the two lists have at least one element in common.")
main()
print('#',75*"-")

# =================================================================
# E.6: Work on a script to merge or join two dictionaries
# =================================================================
print("Homework_E.6:  Work on a script to merge or join two dictionaries")


my_dict1 = {'a': 1, 'b': 2, 'c': "3"}
my_dict2 = {'d': 4, 'e': 5, 'f': "6"}
new_dict = {}
for key in my_dict1.keys():
    new_dict[key] = my_dict1[key]

for key in my_dict2.keys():
    new_dict[key] = my_dict2[key]

print("Dictionary 1", my_dict1)
print("Dictionary 2", my_dict2)
print ("Combined dictionary", new_dict)

print('#',75*"-")
# =================================================================
# E.7: Work on a script or a program to map two lists into a dictionary.
# =================================================================
print("Homework_E.7: Work on a script or a program to map two lists into a dictionary.")
# list #1
keys = ["un", "deux", "trois", "quatre", "cinq"]
# list #2
values = ["one", "two", "three", "four", "five"]

# uses zip method to combine the two lists into a dictionary called new_dict
new_dict = {}
num1 = len(keys)

for i in range(0,num1):
    new_dict[keys[i]] = values[i]
print("list 1", keys)
print("list 2", values)
print("New dictionary", new_dict)
print('#',75*"-")
# =================================================================
# E.8: Answer all the class exercise questions and submit it (Check the instructions).
# =================================================================

# Lecture 2 Exercises
# =================================================================
# Class_Ex1:
# Write a program that simulates the rolling of a die.
# ----------------------------------------------------------------
import random
print("Class_Ex1: Write a program that simulates the rolling of a die.")

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
# loop through a tuple to create a string
test_string = ""
for i in t:
    test_string += i
print("Tuple: ", t)
print("String: ",test_string)
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
