# =================================================================
# Class_Ex1:
# Write a program that simulates the rolling of a die.
# ----------------------------------------------------------------
import random

random.seed(33)
die = random.randint(1, 6)
print(die)
print('#',75*"-")
# =================================================================
# Class_Ex2:
# Answer  Ex1 by using functions.
# ----------------------------------------------------------------

def roll_die():
    import random
    die = random.randint(1, 6)
    print(die)

roll_die()
print('#',75*"-")

# =================================================================
# Class_Ex3: 
# Randomly Permuting a List
# ----------------------------------------------------------------

def random_permute(a):
    import random
    new_list= a[:]
    random.shuffle(new_list)
    print("New list: ", new_list)


original_list = [1, 8, 99, 17]
print("Original list: ", original_list)
random_permute(original_list)
print('#',75*"-")

# =================================================================
# Class_Ex4:
# Write a program to convert a tuple to a string.
# ----------------------------------------------------------------

t = tuple("lupins")
print("Print tuple: ", t)
print(''.join(t))
print('#',75*"-")

# =================================================================
# Class_Ex5:
# Write a program to get the 3th element of a tuple.
# ----------------------------------------------------------------
t = tuple("lupins")
print(t[2])
print('#',75*"-")

# =================================================================
# Class_Ex6:
# Write a program to check if an element exists in a tuple or not.
# ----------------------------------------------------------------
t = tuple("lupins")
n = "1"
if n in t:
    print("Yes, element", n, "is in tuple", t)
else:
    print("No, element", n, "is not in tuple", t)
print('#',75*"-")

# =================================================================
# Class_Ex7:
# Write a program to check a list is empty or not.
# ----------------------------------------------------------------

mylist = ['a', 8.9, 99, [10,20]]

if not mylist:
    print("List is empty")
else:
    print("List is not empty= ", mylist)

print('#',75*"-")
# =================================================================
# Class_Ex8:
# Write a program to generate a 4*5*3 3D array that each element is O.
# ----------------------------------------------------------------

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

print(my_3D_array)
print('#',75*"-")

