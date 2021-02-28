
# Lydia Teinfalt
# DATS 6103: Data Mining
# Spring 2021
# 02/27/2021
# Homework 4 and Lecture 4_1 Exercises
# Reference: https://www.w3resource.com/python-exercises/numpy/basic/index.php
# =================================================================
import numpy as np
import matplotlib.pyplot as plt
print("Solution HW4 and Lecture 4_1 Exercises")
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





# =================================================================
# Lydia Teinfalt
# DATS 6103: Data Mining
# Spring 2021
# 02/27/2021
# Class-Ex-Lecture4_2: Matplotlib
# Find the slope of the following curve for each of its points
#                  y = np.exp(-x ** 2)
# Then plot it with the original curve np.exp(-X ** 2) in the range
# (-3, 3) with 100 points in the range
# ----------------------------------------------------------------
print("Class-Ex-Lecture4_2: Matplotlib")

#Solution Class_Ex1
import numpy as np
import matplotlib.pyplot as plt
x5 = np.linspace(-3, 3, 100)
y5 = np.exp(-x5 ** 2)
plt.plot(x5, y5)
plt.title("Fig 1: exp(-x**2)")
plt.show()

def plt_slope(x,y):
    xs = x[1: ] - x[:-1]
    ys = y[1: ] - y[: -1]
    plt.plot(x[1:], ys/xs, color = "gold")
    plt.title("Figure 2: Slope of exp(-x**2)")
    plt.show()

plt_slope(x5,y5)
print('#',50*"-")




# =================================================================
# Class_Ex2:
# A file contains N columns of values, describing N–1 curves.
# The first column contains the  x coordinates, the second column
# contains the y coordinates of the first curve, the third
# column contains the y coordinates of the second curve, and so on.
#  We want to display those N–1 curves.

# ----------------------------------------------------------------
# Solution Class_Ex2
x= []
y1 = []
y2 = []
for line in open('data2.txt', 'r'):
    data = [float(s) for s in line.split()]
    x.append(data[0])
    y1.append(data[1])
    y2.append(data[2])
plt.plot(x, y1, color = "green")
plt.title("Class Ex_2, Figure 1: X x Y")
plt.show()

plt.title("Class Ex_2, Figure 2: X x Y2")
plt.plot(x, y2, color = "orange")
plt.show()

print('#',50*"-")



# =================================================================
# Class_Ex3: 
# Write a efficient code to stack any number of layers of data into
# a bar chart plot.
# Use the following data.
# ----------------------------------------------------------------
# Solution Class_Ex3
data = np.array([[4,0,4],[1,2,2], [1,2,1], [1,1,0], [0,1,1]])
x = np.arange(3)
colors = ['b', 'g', 'r', 'k', 'y']
bot = np.cumsum(data, axis = 0)
plt.bar(x, data[0], color=colors[0])
for j in range(1, data.shape[0]):
    plt.bar(x, data[j], color=colors[j], bottom=bot[j-1])
plt.show()
print('#',50*"-")

# =================================================================
# Class_Ex4:
# Write a Python code to plot couple of lines
# on same plot with suitable legends of each line.
# ----------------------------------------------------------------
# Solution Class_Ex4
x4= np.linspace(-3,3, 100)
y4_1 = 2*x4 + 1
y4_2 = np.exp(-x4 ** 2)
y4_3 = np.sin(x4)
labels = ("y=2x+1", "exp(-x squared)", "sin(x)")
plt.plot(x4,y4_1,color ="green")
plt.plot(x4,y4_2, color = "blue")
plt.plot(x4,y4_3, color= "Red")
plt.legend(labels)
plt.title("Class Ex4, Figure 1: Line plots with legend")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
print('#',50*"-")





# =================================================================
# Class_Ex5:
# Write a Python code to plot two or more lines with legends,
# different widths and colors.
# ----------------------------------------------------------------
# Solution Class_Ex5
x5= np.linspace(-3,3, 100)
y5_1 = 2*x5 + 1
y5_2 = np.exp(-x5 ** 2)
y5_3 = np.sin(x5)
labels = ("y=2x+1", "exp(-x squared)", "sin(x)")
colors = ("cyan", "orange", "yellow")
plt.plot(x5,y5_1,color =colors[0], label = labels[0], linewidth = 1.5, linestyle = 'dashed')
plt.plot(x5,y5_2, color = colors[1], label = labels[1], linewidth = 3)
plt.plot(x5,y5_3, color= colors[2], label= labels[2], linewidth = 8.7)
plt.legend(labels)
plt.title("Class_Ex5, Figure 1: Line plots with legend, Diff Widths, Diff Colors")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
print('#',50*"-")




# =================================================================
# Class_Ex6:
# Write a Python code to plot two or more lines and set the line markers.
# ----------------------------------------------------------------
# https://www.w3resource.com/graphics/matplotlib/basic/matplotlib-basic-exercise-8.php
# x axis values
x6 = [1,4,5,6,7]
# y axis values
y6_1 = [2,6,3,6,3]
y6_2 = [4,2,1,5,1]

# plotting the points
plt.plot(x6, y6_1, color='red', linestyle='dashdot', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
plt.plot(x6, y6_2, color='green', linestyle = 'dashdot', linewidth = 4, marker='o',markerfacecolor = 'black', markersize = 13)
#Set the y-limits of the current axes.
plt.ylim(1,8)
#Set the x-limits of the current axes.
plt.xlim(1,8)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('Class_Ex6: Display marker')
# function to show the plot
plt.show()
print('#',50*"-")





# =================================================================
# Class_Ex7:
# Write a Python code to show grid and draw line graph of
# revenue of certain companies between November 4, 2017 to November 4, 2018.
# Customized the grid lines with linestyle -, width .6. and color blue.
# ----------------------------------------------------------------
# Solution Class_Ex7
# Reference: https://www.w3resource.com/graphics/matplotlib/basic/matplotlib-basic-exercise-14.php

# Solution Class_Ex7
# Reference: https://www.w3resource.com/graphics/matplotlib/basic/matplotlib-basic-exercise-14.php
# Reference: https://medium.com/@sambit9238/intro-to-data-visualization-using-matplotlib-in-python-8a4068ba48f6

months = ['nov-17','dec-17','jan-18','feb-18','mar-18','apr-18','may-18','jun-18','jul-18','aug-18','sep-18','oct-18', 'nov-18']
revenue_a = np.array([14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50, 1600.7])
revenue_b = np.array([4000, 6000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000])
plt.plot(revenue_a, color="black", ls="--", marker="o", ms=6, label="revenue_companyA")
plt.plot(revenue_b, color="red", ls="--", marker="o", ms=6, label="revenue_companyB")
plt.grid(linestyle='-', linewidth='0.6', color='blue')
plt.xticks(list(range(13)), months, rotation="vertical")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.title("Revenue of Company A & B from Nov-2017 through Nov-2018")
plt.show()
print('#',50*"-")

# =================================================================
# Class_Ex8:
# Write a Python code to create multiple empty plots in one plot
# (facets)
# ----------------------------------------------------------------
# Solution Class_Ex8
# Reference: https://www.oreilly.com/library/view/python-data-science/9781491912126/ch04.html
plt.subplots(2, 3, sharex='col', sharey='row')
plt.show()
print('#',50*"-")






# =================================================================
# # Lydia Teinfalt
# # DATS 6103: Data Mining
# # Spring 2021
# # 02/27/2021
# # Class-Ex-Lecture4_3: Seaborn
# We will be working with a famous titanic data set for these exercises.
# Later on in the Data mining section of the course, we will work  this data,
# and use it to predict survival rates of passengers.
# For now, we'll just focus on the visualization of the data with seaborn:

# use seaborn to load dataset
# ----------------------------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic') #load titanic
# =================================================================
# Class_Ex2:
# Join plot on fare and age
# ----------------------------------------------------------------
# Solution Class_Ex2
sns.jointplot(x=titanic['fare'], y=titanic['age'])
plt.show()



# =================================================================
# Class_Ex3:
# Distribution plot on fare with red color and 35 bin
# ----------------------------------------------------------------
# Solution Class_Ex3:
sns.distplot(x=titanic['fare'], color="red", bins=35)
plt.show()



# =================================================================
# Class_Ex4:
# box plot on class and age
# ----------------------------------------------------------------
# Solution Class_Ex4
# Reference: https://notebook.community/luizhsda10/Data-Science-Projectcs/Data%20Visualization/Seaborn/Seaborn%20Practice%20-%20Titanic%20Data
sns.boxplot(x=titanic['class'],y=titanic['age'],palette='rainbow')
plt.show()

# =================================================================
# Class_Ex5:
# swarmplot on class and age
# ----------------------------------------------------------------
# Solution Class_Ex5
# Reference: https://notebook.community/luizhsda10/Data-Science-Projectcs/Data%20Visualization/Seaborn/Seaborn%20Practice%20-%20Titanic%20Data
sns.swarmplot(x=titanic['class'], y=titanic['age'], palette="rainbow")
plt.show()




# =================================================================
# Class_Ex6:
# Count plot on sex
# ----------------------------------------------------------------
sns.countplot(x=titanic['sex'])
plt.show()




# =================================================================
# Class_Ex7:
# plot heatmap
# ----------------------------------------------------------------
# Solution Class_Ex7
sns.heatmap(titanic.corr(),cmap='coolwarm')
plt.title('titanic.corr()')
plt.show()




# =================================================================
# Class_Ex8:
# Distribution of male and female ages in same grapgh (Facet)
# ----------------------------------------------------------------
g = sns.FacetGrid(data=titanic,col='sex')
g.map(plt.hist,'age')
plt.show()




# =================================================================
# Class_Ex9:
# Explain each graph and describe the results in words
# ----------------------------------------------------------------

print("Joint plot shows relationship between passengers' ages and fare prices ")
print("along with the histograms age and fares.")
print("Distribution plot of fare prices to determine the distribution.")
print("Box plots showed the age of passengers in first, second and third classes.")
print("Box plot give visual on range, max, min and median values of the ages in each class.")
print("Swarm plots used to determine relationship between age and categorical data of first, second and third classes. ")
print("Count plots are similar to histograms broken down by passenger's gender.")
print("Heat map showing how much or little features in the titanic correlate. ")
print("Two histogram showing ages of titanic passengers broken down by gender. ")



