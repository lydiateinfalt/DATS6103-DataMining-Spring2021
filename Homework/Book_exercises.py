# # Lydia Teinfalt
# # DATS 6103: Data Mining
# # Spring 2021
# # 02/01/2021
# # Homework 2 Exercises
# # Write a function called is_sorted that takes a list as a parameter and returns True
# # if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that
# # the elements of the list can be compared with the relational operators <, >, etc.
# # For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should return
# # False.
# def is_sorted(l):
#     l1= []
#     l1 = sorted(l)
#     if l == l1:
#         return True
#     else:
#         return False
#
# # my_list = [1,2,2]
# my_list = ['b','a']
# if is_sorted(my_list):
#     print("List 1", my_list, " is sorted")
# else:
#     print("List 1", my_list, " is not sorted")
#
# # Exercise 10.7. Two words are anagrams if you can rearrange the letters from one to spell the other.
# # Write a function called is_anagram that takes two strings and returns True if they are anagrams.
#
# def is_anagram(l1, l2):
#     print(l1[::-1])
#     if l2 == l1[::-1]:
#         print("True")
#     else:
#         print("False")
#
# print(is_anagram('realtor', 'rotlaer'))
# print(is_anagram('hydro', 'ordyh'))
#
# def has_duplicates(list1):
#     if len(list1) == len(set(list1)):
#         return False
#     else:
#         return True
#
# print(has_duplicates([1, 2, 'Amir', 19, -3, 'Amir', 'end']))
#
#
# # Ask the user for a number.
# # Depending on whether the number is even or odd,
# # print out an appropriate message to the user.
# # Hint: how does an even / odd number react differently when divided by 2?
# #
# # Extras:
# #
# # If the number is a multiple of 4, print out a different message.
# # Ask the user for two numbers:
# # one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
#
# def odd_even(num):
#     attr = ""
#     if num % 4 == 0:
#         attr = "multiple4"
#     elif num % 2 == 0:
#         attr = "even"
#     else:
#         attr = "odd"
#     return attr
#
# num = eval(input("Please enter a number: "))
# result = odd_even(num)
# if result == "even":
#     print("Number is even")
# elif result == "multiple4":
#     print("Number is a multiple of 4")
# else:
#     print("Number is odd")
#
# ####
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [x for x in a if x < 10]
# print(b)
#
# num = int(input("Please choose a number to divide: "))
# list1= []
# listRange = list(range(1,num+1))
# for x in listRange:
#      if num % x == 0:
#          list1.append(x)
#
# print(list1)
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


