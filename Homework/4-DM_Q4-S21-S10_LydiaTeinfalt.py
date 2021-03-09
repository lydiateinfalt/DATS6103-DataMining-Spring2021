# Lydia Teinfalt
# Quiz 4
# DATS 6103, Spring 2021
# 03/09/2021

# %% 1- Download the data_1 zip file from Blackboard. unzip the zip file by using zipfile package.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q1" + 20* "-")
import zipfile
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# importing required modules
# Reference: https://www.geeksforgeeks.org/working-zip-files-python/

# specifying the zip file name
file_name = "data_1.zip"
cwd = os.getcwd()
# opening the zip file in READ mode
with zipfile.ZipFile(file_name, 'r') as zip:
    floc = cwd + '\\data_1'
    zip.extractall(floc)


# %% 2- Extract the the zip file using zipfile package and store the content into a data_1 folder (it has to be done automatically by os package).
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q2" + 20* "-")
#extracted files to \data_1 directory
os.chdir(floc)
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

# %% 3- Read all the csv files and search for the csv file which has "Team" as column header.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q3" + 20* "-")
# Read each file in data_1 directory until we find "Team" in the list of columns
for file in files1:
    data = pd.read_csv(file)
    if "Team" in list(data.columns.values):
        print("Data file with 'Team' in the list of columns: ", file)
    else:
        carat = data

# %% 4- Search for the followings.
# i. Find all the list of all unique teams and print out the total number.
# ii. Who gets the most salary and find out his age, position, and team .
# iii. Is there any trend between salary and age. Use linear regression and explain your results.

# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q4" + 20* "-")
# Reference: https://data36.com/linear-regression-in-python-numpy-polyfit/

x = data.groupby(['Team']).agg({'Team': 'count'})
print("Total number of unique teams:", x.size)

salary_column = data['Salary']
max_salary = salary_column.max()
richest=data[data.Salary == max_salary]
print("Highest salary is earned by:", data[data.Salary == max_salary])
print("Age:")
print(richest['Age'].values[0])
# print(richest.Age[0].values.tolist())
print("Position:")
# print(richest.Position.values.tolist())
print(richest['Position'].values[0])
print("Team:")
print(richest.Team.values[0])


plt.scatter(data['Salary'], data['Age'])
plt.xlabel('Salary')
plt.ylabel('Age')
plt.title("Figure 1 Scatter plot Salary x Age")
plt.figure(1)
plt.show()
data = data.dropna()
print(data)
x = np.array(data['Salary'])
y = np.array(data['Age'])

#Linear regression
m, b = np.polyfit(x,y,1)
plt.plot(x, y, 'yo', x, m*x+b, '--k')

plt.xlabel('Salary')
plt.ylabel('Age')
plt.title("Figure 2 Salary x Age with Best Fit Line")
plt.figure(2)
plt.show()
print("Using Figure 2 between Salary x Age with shows that there appears to be no clear linear relationship.")
# %% 5- Read the other csv file and answer the following questions.
# i. Sort the entire DataFrame by the 'carat' Series in ascending and descending order.
# ii. Get randomly sample rows from diamonds DataFrame.
# iii. Get sample 75% of the DataFrame's rows without replacement and store the remaining 25% of the rows in another DataFrame.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q5" + 20* "-")


print("Ascending order")
print(carat.sort_values(by='carat',ascending=True))
print("Descending order")
print(carat.sort_values(by = 'carat',ascending=False))

print("Randomly sample row")
print(carat.sample())
print()
print("Five randomly sample rows")
print(carat.sample(5))
print()
# Reference: https://www.geeksforgeeks.org/how-to-randomly-select-rows-from-pandas-dataframe/
print("Get sample 75%\n", carat.sample(frac=0.75, replace=False))

carat1 = carat.sample(frac=0.25, replace = True)


print("Remaining 25%\n", carat1)
