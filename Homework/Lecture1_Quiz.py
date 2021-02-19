# Lydia Teinfalt
# DATS 6103: Spring 2021
# Quiz 1
# =================================================================
# Write a python script that find items from the first list (temp1) which are not in the
# second list (temp2).
# Note: DO NOT manually print each digits. Write script in a way that can accept
# any list.
# =================================================================

temp1 = [4 , 5 , 6 , 7]
temp2 = [4 , 5]

def element_in_common(l1, l2):

    m = len(l1)
    n = len(l2)
    l = ()
    for i in range (0, m):
        if l1[i] not in l2:
            l= l1[i]
    return l

def main():
    temp1 = [4, 5, 6, 7]
    temp2 = [4, 5]
    new_list = []
    new_list = element_in_common(temp1, temp2)
    print(new_list)
main()
print('#',75*"-")

# =================================================================
# Question 2:
# Write at least 2 python script that reverse the following list elements.
# Note: DO NOT use any packages. You can use for loops and if conditions or python
# basic built in functions.
# =================================================================

def reverse(l):
    return [ele for ele in reversed(l)]

def main():
    ls = [ 'a', 'b ', 'c ', 'd']
    modified_l = []
    modified_l = reverse(ls)
    print(modified_l)

main()

# =================================================================
# Question 3:
# Write a phyton script that create a sequence of numbers in which, the next number
# is found by adding up the two numbers before it.
# Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# =================================================================

def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(10)

# =================================================================
# Question 4:
# Write a python script that finds numbers and the capital words int he following string
# and save them into a separate lists.
# Strings = [ ’ Guido van Rossum born 31 January 1956 is a
# Dutch programmer best known as the creator
# of the Python programming language ’]
# =================================================================

def main():
    '''

    :return: Returns a dictionary in no order of display the number of times a character appears in the sample string
    '''
    # Sample string
    input_string = "Guido van Rossum born 31 January 1956 is a Dutch programmer best known as the creator of the Python programming language"

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


str = input("Please enter line of text: ")
ls = []
# An acronym is a word formed by taking the first letters of the words in a phrase and making a word from them.
# For example, RAM is an acronym for random access memory.
# Write a program that allows the user to type in a phrase and then outputs the acronym for that phrase.
# Note: The acronym should be all uppercase, even if the words in the phrase are not capitalized.

str1 = input("Please enter line of text: ")
str1 = str1.upper()
acronym = []
for i in str1.split():
    acronym += i[0]
str2 = ""
str2 = acronym
print(str2)
