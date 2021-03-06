
# Lydia Teinfalt
# DATS 6103: Data Mining
# Spring 2021
# 02/27/2021
# Homework 4 and Lecture 4_1 Exercises
# Reference: https://www.w3resource.com/python-exercises/numpy/basic/index.php
# =================================================================
import numpy as np
import matplotlib.pyplot as plt
Print("Solution HW4 and Lecture 4_1 Exercises")
# =================================================================
print('#',50*"-")
# Solution E.1
print('#', 75 * "-")
print("HW_E.1:  Write a script to "
      "i. sum all the items in a array (use random generator and multiply it by 100,"
      "create a vector with the size 200")
print()

e100 = np.random.randint(1, 10, size=200) * 100
print("Array:", e100)
sum = np.sum(e100)
print("i. Sum:", sum)

e1_min = np.min(e100)
e1_max = np.max(e100)
print("ii. Largest number: {m} , smallest number: {s}".format(m=e1_max, s=e1_min))
e1_index_min = np.where(e100 == e1_min)
e1_index_max = np.where(e100 == e1_max)
print("Index of smallest num in the array:", e100.tolist().index(e1_min))
print("Index of largest num in the array:", e100.tolist().index(e1_max))
print(e100[ : :-1])

plt.plot(np.arange(0, 200), e100, color = "blue")
plt.show()
print('#',50*"-")
# =================================================================
# Solution E.2: Plot functions x, sin(x), ex, and log(x) over the interval 1 < x < 6 with step size of 0.1

x=np.arange(1, 6, 0.1)
ya = np.sin(x)
plt.ylabel("sinx(x)")
plt.xlabel("x axis")
plt.plot(x, ya, color="blue", label = "sin(x)")
plt.show()

yb = np.exp(x)
plt.ylabel("e(x)")
plt.xlabel("x axis")
plt.plot(x, yb, color = "red", label = "e(x)")
plt.show()


yc = np.log(x)
plt.ylabel("log(x)")
plt.xlabel("x axis")
plt.plot(x, yc, color= 'black', label = "log(x)")
plt.show()

print('#',50*"-")
# =================================================================
# Solution E.3: Generate random gaussian numbers vector x
mu, sigma = 0, 1 # mean and standard deviation
x = np.random.normal(mu, sigma, 100)
# Vector x
print("Vector x\n")
# print(x)
print("Mean of vector x: ", x.mean())
# hx = plt.hist(x, bins=100)
hx = plt.hist(x, bins=20)
plt.xlabel("Vector X Values")
plt.ylabel("Count")
plt.show()

# Vector y
y = np.random.uniform(mu, sigma, 100)

print("Vector y\n")
# print(y)
print("Mean of vector y: ", y.mean())
hy = plt.hist(y, bins=20)
plt.xlabel("Vector y values")
plt.ylabel("Count")
plt.show()

print("The histograms show the counts of numbers falling within the bin size values in the vector x and y. \n")
print("The greater number of bins represent a smaller range of values.")
print('#',50*"-")
# =================================================================
# Solution E.4:
A = np.arange(1,10).reshape(3,3)
print("Matrix A:\n", A)
x = A[0]
print("i. Vector x:\n", x)
y = A[1:]
print("ii. Vector y: \n", y)
A[:,0] = A[:,0] + A[0].sum()
print("iii. Sum the first row and add it to the first column, column values:\n ", A)
print("iv. Compute the norm of x (Euclidian Norm): ", np.linalg.norm(x))
print("Before wap \n")
print(A)
A[:,[1,0]] = A[:,[0,1]]
print("After swap\n", A)
A=np.delete(A,1,0)
print("v. Matrix after delete\n", A)
# =================================================================

# Solution E.5

# i. Create a vector between 20 and 35, square each elements and sum all the elements of this
# vector.
v = np.arange(20,36)
v_square = np.square(v)
print("i.Vector between 20 and 35:\n", v)
print("Square each element:\n", v_square)
print("Sum all elements:", np.sum(v_square))
x = np.array([[2, -4, 9, -8],[-3, 2, -1, 0],[5, 4, -3, 3]])
print(x)
print()
# ii. Compute the absolute value of x for all the rows and columns separately.
print("ii. Compute the absolute value of x for all the rows and columns separately.\n")
x = np.absolute(x)
print(x)
print()
# iii. Compute the square of each elements of x.
print("iii. Compute the square of each element.\n")
print(np.sqrt(x))
print()
# iv. Swap the first row by the second row.
x[[1,0],:] = x[[0,1],:]
print("iv. Swap the first row by the second row. \n",x)
# v. Replace the first row by zeros and the third row by ones.
print("v. Replace the first row by zeros and the third row by ones.\n")
x[0] = np.zeros(4)
x[2] = np.ones(4)
print(x)
print()
# vi. Compute the mean and standard deviation of first and third row.
print("vi. Compute the meand and standard deviation of first and third row.\n")
print(np.mean(x[0]))
print(np.mean(x[2]))
# vii. Sum all the columns and then sum the results.
print("vii. Sum all the columns: \n", np.sum(x, axis=0))
print("Sum:", np.sum(x))
print('#',50*"-")
# =================================================================
# Solution E.6
# Reference: https://www.geeksforgeeks.org/bar-plot-in-matplotlib/
data = {'Java': 22.2, 'Python': 17.6, 'PHP': 8.8, 'JavaScript': 8, 'C#': 7.7, 'C++': 6.7}
languages = list(data.keys())
percentages = list(data.values())
plt.bar(languages, percentages)
#plt.xlabel("Popular programming languages")
#plt.ylabel("Percentages")
plt.show()
print('#',50*"-")

# =================================================================
# Solution E.7
# https://www.w3resource.com/graphics/matplotlib/barchart/matplotlib-barchart-exercise-12.php

N = 4
Avg = (0.14, 0.32, 0.47, 0.38)
STD = (0.23, 0.32, 0.18, 0.46)
# the x locations for the groups
ind = np.arange(N)
# the width of the bars
width = 0.35
plt.bar(ind, Avg, width, yerr=STD)
plt.ylabel('Scores')
plt.xlabel('Velocity')
plt.title('Scores by Velocity')
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()
print('#',50*"-")
# =================================================================
# Solution E.8: Write a script to find the second largest number in an array (use random number generator) nd
# multiply it by 50.
x = np.random.randint(10, size=(4,4))
print(x)
# create an array with numbers smaller than the max value
x = x[x<np.max(x)]
#Print the second highest number from above step
print("Find second highest value in an array and multiply it by 50:", np.max(x) * 50)
print('#',50*"-")
# =================================================================
# E.9:
# Answer all the class exercise questions (Lecture 4 - All) and submit it (Check the instructions).

# Solution Class_Ex1: Write Numpy code to test if none of the elements of an array is zero
# Reference: https://www.w3resource.com/python-exercises/numpy/basic/index.php

def check_np_zeroes(ar):
  #if array does not have any zeroes, it would evalute as true
  if np.all(ar):
    return True
  else:
    return False

# numpy all checks of any elements evaluates to zero. 0 evaluates to false
x = np.array([0, 1, 44, 6, -9])
y = np.array([9, 8, 9, 10])
print(y)
if check_np_zeroes(y):
  print("Numpy array contain no zeroes")
else:
  print("Numpy array does contain zeroes")

print('#',50*"-")

# Solution Class_Ex2: none of the elements of a given array is non-zero
# Reference: https://www.w3resource.com/python-exercises/numpy/basic/index.php
x = [0,0,0,0,0]
print("Original array", x)
print(not np.any(x))
y = [1,0,0,0,0,0]
print("Original array",y)
print(not np.any(y))
print('#',50*"-")


# Solution Class_Ex3: Write a NumPy code to test if two arrays are element-wise equal within a tolerance
# Reference: https://www.w3resource.com/python-exercises/numpy/basic/index.php
ar1 = [0.6, 0.1, -0.0001]
ar2 = [0.4, 0.2, -0.1]
print("Original arrays", ar1, "", ar2)
print(np.isclose(ar1, ar2, rtol=0.1, atol=0.2))
a=[1e10,1.002e10]
b=[1e10,1.003e10]
print("Original arrays", a, "", b)
print(np.isclose(a, b, rtol=1.0001e10, atol=1.0001e10))
a=[0.4,1.002e10]
b=[0.8,1.003e10]
print("Original arrays", a, "", b)
print(np.isclose(a, b,atol=0.00001e11))

print('#',50*"-")

# Solution Class_Ex4
a = np.array([1, 8, 130, 10990005])
print("Input array", a)
print("Memory size of array (bytes)", a.size * a.itemsize)
print('#',50*"-")

#Solution Class_Ex5
x = np.random.randint(10, 20, size = 10)
print("Original array:", x)
print("Modified array without the first or last element", x[1:len(x)-1])


print('#',50*"-")

# Solution Class_Ex6: Numpy code to reverse (flip) an array

y = np.random.randint(0,100, size = 20)
print("Original array", y)
y = y[::-1]
print("Flipped (reversed) array", y)
print('#',50*"-")

# Solution Class_Ex 7: Write a NumPy code to create a matrix with 1 on the border and 0 inside.
# Reference: https://www.w3resource.com/python-exercises/numpy/basic/index.php
xray = np.ones((7,7))
print("Original matrix:", xray)
xray[1:-1,1:-1] = 0
print("Modified:", xray)
print('#',50*"-")


# Solution Class_Ex8: Write a NumPy code to add a border (filled with 0's) around a 3x3 matrix of one.
# Reference: https://www.w3resource.com/python-exercises/numpy/basic/index.php
ray3 = np.ones([3,3])
print("Original matrix:", ray3)
ray3=np.pad(ray3, pad_width=1, mode='constant', constant_values= 0)
print("Modified:\n", ray3)
print('#',50*"-")

# Solution Class_Ex9: Write a NumPy code to append values to the end of an array.
ex9_array = np.array([99, 88, 77])
np.append(arr=ex9_array, values=(66, 55))
print('#',50*"-")

# Solution Class_Ex10: NumPy code to find the set difference of two arrays.
# The set difference will return the sorted, unique values in array1 that are not in array2.

array1 = np.array([21, 16, 6, 26, 1, 13, 21, 1, 15, 28])
array2 = np.array([2, 4, 22, 11, 3, 7, 24, 12, 13, 20])
array3 = np.array([item for item in array1 if item not in array2])
array3 = np.sort(array3)
array3 = np.unique(array3)
print("Array1:", array1)
print("Array2:", array2)
print("Unique values in array 1 that are not in array2\n", array3)
print('#',50*"-")

# Solution Class_Ex11: Write a NumPy code to construct an array by repeating. Sample array: [1, 2, 3, 4, 5]
n = np.array([1, 2, 3, 4, 5])
new_array = np.tile(n,5)
print(new_array)
print('#',50*"-")

# Solution Class_Ex12: Write a NumPy code to get the values and indices of the elements
# that are bigger than 6 in a given array.
x = np.array([1,99, 0, 17, -8, 11, 66])
print("Values bigger than 6 =", x[x>6])
print("Their indices are ", np.where(x > 6))
print('#',50*"-")


# Solution Class_Ex13: Write Numpy code to get the 4th element of a 2 dimensional array
x = np.array([[2,5,7],[8,9,10]])
print("Original array \n")
print(x)
print("4th element of the array:",x.flat[3])
print('#',50*"-")


# Solution Class_Ex14: Write a NumPy code to get the floor, ceiling and truncated values of the elements of an numpy array.
x = [1.52421, 3.1123, - 1.053, 0.04354507, 2.19]
print(x)
print("Floor values:",np.floor(x))
print("Ceiling values:",np.ceil(x))
print("Truncated values:", np.trunc(x))
print('#',50*"-")

# Solution for Class_Ex15: Write a NumPy code to compute the factor of a given array by Singular Value Decomposition.
# Reference: https://www.w3resource.com/python-exercises/numpy/linear-algebra/numpy-linear-algebra-exercise-18.php

x = np.array([[3, 4, 1, 4], [4, 2, 3, 2], [3, 0, 4, 4], [3, 2, 4, 4]])
print(x)
U, s, V = np.linalg.svd(x, full_matrices=False)
q, r = np.linalg.qr(x)
print("Factor of a given array  by Singular Value Decomposition:")
print("U=\n", U, "\ns=\n", s, "\nV=\n", V)
print('#',50*"-")

# Solution Class_Ex16: Write a NumPy code to compute the eigenvalues and right eigenvectors of a given square array.
# Reference: https://www.w3resource.com/python-exercises/numpy/linear-algebra/numpy-linear-algebra-exercise-18.php
x = np.array([[1, 3, 5],
              [2, 1, 0],
              [2, 4, 6]])
y,z = np.linalg.eig(x)
print("Eigenvalues", y)
print("Right eigenvalues\n", z)
print('#',50*"-")


# Solution CLass_Ex17: Write a NumPy code to get the dates of yesterday, today and tomorrow.
# https://www.w3resource.com/python-exercises/numpy/python-numpy-datetime-exercise-2.php
today = np.datetime64("today")
yesterday = today - np.timedelta64(1, 'D')
tomorrow = today + np.timedelta64(1, 'D')
print(yesterday)
print(today)
print(tomorrow)
print('#',50*"-")

# Solution Class_Ex18: Write a NumPy code to find the first Monday in June 2021.
# https://www.w3resource.com/python-exercises/numpy/python-numpy-datetime-exercise-5.php
print("First Monday in June 2021:")
print(np.busday_offset('2021-06', 0, roll='forward', weekmask='Mon'))
print('#',50*"-")

print('#',50*"-")
# Solution Class_Ex19:
# Write a NumPy code to find the roots of the following polynomials.
# a) x2 − 3x + 8.
# b) x4 − x3 + -x2 + 1x – 2
# https://www.w3resource.com/python-exercises/numpy/python-numpy-math-exercise-16.php

print(np.roots([1,-3]))
print(np.roots([1, -1, -1, 1]))

print('#',50*"-")


# Solution Class_Ex20: Write a NumPy program to calculate mean across dimension, of matrix.
x = np.arange(12).reshape((3, 4))
print(x)

print(x.mean())
# print(x.mean(0))
# print(x.mean(1))
print(x.mean(axis=0))
print(x.mean(axis=1))
print('#',50*"-")




