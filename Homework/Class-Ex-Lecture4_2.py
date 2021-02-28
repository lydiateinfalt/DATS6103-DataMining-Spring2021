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





