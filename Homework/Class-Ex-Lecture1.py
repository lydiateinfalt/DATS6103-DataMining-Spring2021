# Lydia Teinfalt
# DATS 6103: Data Mining
# Spring 2021
# 1/21/2021
#=================================================================
# Class_Ex1:
# Write python program that converts seconds to
# (x Hour, x min, x seconds)
# ----------------------------------------------------------------
#
print("=================================================================")
print("Class_Ex1")
seconds = eval(input('Enter the time in seconds (positive integer please): '))
hours = (seconds // 3600)

if ((hours)) <= 0:
    minutes = seconds // 60
    seconds = seconds - (minutes * 60)
else:
    minutes = (seconds - (hours * 3600)) // 60
    seconds = seconds - (hours * 3600) - (minutes * 60)

print("Converted time: ", hours, "hour(s)", minutes, "minute(s)", seconds, "seconds")

# =================================================================
# Class_Ex2:
# Write a python program to print all the different arrangements of the
# letters A, B, and C. Each string printed is a permutation of ABC.
# ----------------------------------------------------------------
def swap(char, i, j):
    temp = char[i]
    char[i] = char[j]
    char[j] = temp
    return char


def permute(str, left, right):
    if left == right:
        print_string = " "
        print(print_string.join(str))
    else:
        row: int
        for index in range(left, right):
            swap(str, left, index)
            permute(str, left + 1, right)
            # backtrack
            swap(str, left, index)


x = "ABC"
print("=================================================================")
print("Class_Ex2")
print("String =", x)
x_length = len(x)
x_list = list(x)
permute(x_list, 0, x_length)


# =================================================================
# Class_Ex3:
# Write a python program to print all the different arrangements of the
# letters A, B, C and D. Each string printed is a permutation of ABCD.
# ----------------------------------------------------------------
#
def swap(char, i, j):
    temp = char[i]
    char[i] = char[j]
    char[j] = temp
    return char


def permute(str, left, right):
    if left == right:
        print_string = " "
        print(print_string.join(str))
    else:
        row: int
        for index in range(left, right):
            swap(str, left, index)
            permute(str, left + 1, right)
            # backtrack
            swap(str, left, index)


x = "ABCD"
print("=================================================================")
print("Class_Ex3")
print("String =", x)
x_length = len(x)
x_list = list(x)
permute(x_list, 0, x_length)

# =================================================================
# Class_Ex4:
# Suppose we wish to draw a triangular tree, and its height is provided
# by the user.
# ----------------------------------------------------------------

print("=================================================================")
print("Class_Ex4")
rows=eval(input('Please specify the height or the number of rows the tree should have: '))
j = rows-1
end=rows*2-1
print(end='')
for i in range(1,end+1,2):
     print(' '*j+i*'*')
     j=j-1


# =================================================================
# Class_Ex5:
# Write python program to print prime numbers up to a specified values.
# ----------------------------------------------------------------
def isprime(n):
    prime = bool
    for j in range(2, n):
        m = n % j
        if m != 0:
            prime = True
        elif m == 0:
            prime = False
            return prime
            break
    return prime


print("=================================================================")
print("Class_Ex5: Write python program to print prime numbers up to a specified values. ")
upper = eval(input('Enter max number for prime number list: '))
print("Max number = ", upper)
print('List of prime numbers')
if upper >= 1 and type(upper) == int:

    for i in range(2, upper+1):
        if isprime(i) or i == 2:
            print(i)
else:
    print("Please enter an integer equal to 1 or greater")
