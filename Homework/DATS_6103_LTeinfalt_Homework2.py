# Lydia Teinfalt
# DATS 6103: Data Mining
# Spring 2021
# 01/21/2021
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
print("Homework_E.1:")
import math

def guess_calc(min, max):
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
    # l = [11, 22, 33, 44, 55]

    # example of a list where the algorithm will not work
    l = [99, 88, 77, 66, 55, 44, 22]
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
    input_string = "Documentsinabriefcasesssd"
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
    n = len(l1)
    temp_len = 0
    max_len = 0
    for i in range(0, n):
        temp_len = len(l1[i])
        if temp_len > max_len:
            max_len = temp_len
    return max_len

def main():
    l = ["Unless", "you're", "Python", "unanimous"]
    longest = find_longest_word(l)
    print("Longest word length", longest)

main()
print('#', 75*"-")

# =================================================================
# E.4:
# Make up your own list and work on a program to get the smallest number from the list.
# =================================================================
print("Homework_E.4: Make up your own list and work on a program to get the smallest number from the list.")


def main():
    l_num = [99,1,45,3,8, 50, -1, -100]
    l_num.sort()
    print("List", l_num)
    print("Smallest in list", l_num[0])

main()

print('#', 75*"-")
# =================================================================
# E.5:
# Work on a function that takes two lists and returns same (or True) if they have at least one
# common element.
# =================================================================
print("Homework_E.5: Work on a function that takes two lists and returns same (or True) if they have at least one.")

def element_in_common(l1, l2):
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
    if element_in_common(test_list1, test_list2):
        print("Yes, the two lists have at least one element in common.")
main()
print('#',75*"-")

# =================================================================
# E.6: Work on a script to merge or join two dictionaries
# =================================================================
print("Homework_E.6:  Work on a script to merge or join two dictionaries")

def merge(d1, d2):
    return(d2.update(d1))


my_dict1 = {'a': 1, 'b': 2, 'c': "3"}
my_dict2 = {'d': 4, 'e': 5, 'f': "6"}
print(merge(my_dict1, my_dict2))
print(my_dict2)

print('#',75*"-")
# =================================================================
# E.7: Work on a script or a program to map two lists into a dictionary.
# =================================================================
print("Homework_E.7: Work on a script or a program to map two lists into a dictionary.")
keys = ["un", "deux", "trois", "quatre", "cinq"]
values = ["one", "two", "three", "four", "five"]
new_dict=dict(zip(keys,values))
print(new_dict)
print('#',75*"-")
# =================================================================
# E.8: Answer all the class exercise questions and submit it (Check the instructions).
# =================================================================

