# =================================================================
# Class_Ex1: 
# Write python program that converts seconds to 
# (x Hour, x min, x seconds)
# ----------------------------------------------------------------
#
print("=================================================================")
print("Class_Ex1")
seconds = eval(input('Enter the time in seconds (positive integer please): '))
hours = (seconds // 3600)
print("Entered time in seconds = ", seconds)

if ((hours)) <= 0:
     minutes = seconds // 60
     seconds = seconds - (minutes * 60)
 else:
     minutes = (seconds - (hours * 3600)) // 60
     seconds = seconds - (hours * 3600) - (minutes * 60)


print("Converted")
print("Hour(s) = ", hours)
print("Minute(s) = ", minutes)
print("Second(s) =", seconds)


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
# def swap(char, i, j):
#     temp = char[i]
#     char[i] = char[j]
#     char[j] = temp
#     return char
#
#
# def permute(str, left, right):
#     if left == right:
#         new_string = " "
#         print(new_string.join(str))
#     else:
#         row: int
#         for index in range(left, right):
#             swap(str, left, index)
#             permute(str, left + 1, right)
#             # backtrack
#             swap(str, left, index)

print("=================================================================")
print("Class_Ex3")
y = "ABCD"
print("String =", y)
y_len = len(y)
y_list = list(y)
permute(y_list, 0, y_len)

# =================================================================
# Class_Ex4: 
# Suppose we wish to draw a triangular tree, and its height is provided 
# by the user.
# ----------------------------------------------------------------


# =================================================================
# Class_Ex5: 
# Write python program to print prime numbers up to a specified values.
# ----------------------------------------------------------------


# =================================================================
