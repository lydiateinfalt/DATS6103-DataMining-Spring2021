# =================================================================
# Lydia Teinfalt
# DATS 6103, Spring 2021
# Homework 5, 03/03/21
# ----------------------------------------------------------------
# Work with Pandas module and answer the following questions. Open a .py file and follow the
# instructions and write codes for each section.


# Solution HW_Ex1
# i. Import Pandas and libraries that you think it is needed.
import pandas as pd
import numpy as np
print("Solution HW_Ex1")
# ii. Import the dataset from BB. The name of the dataset is Data2.txt.
chipotle = pd.read_csv("data2.txt", sep="\t" )

# iii. Assign it to a variable called chipotle and print the 6 observation of it.
print(chipotle['item_price'])
print(chipotle.head(6))

# iv. Clean the item price column and change it in a float data type then reassign the column with
# the cleaned prices.
chipotle['new_item_price'] = chipotle['item_price'].str.lstrip('$').astype(float)
# print(chipotle['new_item_price'])
chipotle['item_price'] = chipotle['new_item_price']

# v. Remove the duplicates in item name and quantity.
chipotle.drop_duplicates(subset=['item_name'])
chipotle.drop_duplicates(subset=['quantity'])
# print(chipotle)
# vi. Find only the products with quantity equals to 1 and find item price that greater that 10.
print(chipotle[chipotle.quantity == 1 & (chipotle.item_price > 10)])

# vii. Find the price of each item.
item_list = pd.DataFrame(chipotle[chipotle.quantity == 1], columns=['item_name', 'item_price'])
chipotle_menu = item_list.drop_duplicates(keep=False).sort_values(by=['item_name'])
print("Item name - price", chipotle_menu)

# ix. find the most expensive item ordered.
column = chipotle['item_price']
max_value = column.max()
print("Most expensive item ordered: $",max_value)

# x. Find the frequency of times were a Veggie Salad Bowl ordered.
dfx = chipotle[(chipotle['item_name'] == 'Veggie Salad Bowl')]
print("Number of orders for Veggie Salad Bowl:", dfx.shape[0])


print(chipotle['item_price'].aggregate(np.sum))
# xi. How many times people ordered more than one Canned Soda?
# chipotle.loc[(chipotle['item_name'] == 'Canned Soda') & (chipotle['quantity'] > 1)]
dfxi = chipotle.loc[(chipotle['item_name'] == 'Canned Soda') & (chipotle['quantity'] > 1)]
print("Number of orders where the number of 'Canned Soda' ordered greater than one:", dfxi.shape[0])
print('#',50*"-")
# ----------------------------------------------------------------

# E.2:
# Work with Pandas module and answer the following questions. Open a .py file and follow the
# instructions and write codes for each section.
# i. Import Pandas and libraries that you think it is needed.
# ii.Import the dataset from BB. The name of the dataset is Food.txt.
# iii. Print the size of the data frame and the6 observation of it.
# iv. How many columns this dataset has and print the name of all the columns.
# v. What is the name and data type of 105th column?
# vi. What are the indices of this datset. How they are shaped and ordered.
# vii. What is the name of product of 100th observation .

# panda already imported above as pd
food = pd.read_csv("food.tsv", sep="\t" )
print("Solution HW_E.2")
print("iii. Food dataframe size:", food.size)
print("iii. Number of rows:", food.shape[0])
print("iv. Number of columns:", food.shape[1])
print("iv. Column names:", list(food.columns.values))
print("v. Column 105 name:", food.columns.values[105])
print("v. Column 105 data type:", food.iloc[:, 105].dtypes)
print("vi. Indices:", food.index.values)
print("vi. Index shape:", food.index.shape)
print("vi. Index sorted increasing?:", food.index.is_monotonic_increasing)
print("vi. Index sorted decreasing?:", food.index.is_monotonic_decreasing)
print("v. Product name at 100th position:", food['product_name'].iloc[100])
print('#',50*"-")
# ----------------------------------------------------------------
# Solution HWE.3:
# Work with Pandas module and answer the following questions. Open a .py file and follow the
# instructions and write codes for each section.

print("Solution HW_E.3")
# i. Import Pandas and libraries that you think it is needed.
# import pandas as pd # pandas already imported above
import numpy as np
# ii. Import the dataset from BB. The name of the dataset is Data.txt.
users = pd.read_csv("Data.txt", sep="|")
# iii. Assign it to a variable called users and print the 6 observation of it.
print(users.head(6))
# iv. Find what is the mean age for occupation.
print(users.groupby(['occupation']).mean())
# v. Find the male ratio for occupation and sort it from the most to the least.
m = users[users.gender == 'M'].groupby('occupation').count()
t = users.groupby('occupation').count()
ratio = m/t
# print(m.gender)
# print(t.gender)
print("v. Find the male ratio for occupation, display desc order",ratio.gender.sort_values(ascending=False))

# vi. For each occupation, calculate the minimum and maximum ages.
# vi. For each occupation, calculate the minimum and maximum ages.
u6 = users.groupby(['occupation']).agg({ 'age' : ['min' , 'max' ]})
print("vi. Min/max age by occupation:")
print(u6)

# vii.For each combination of occupation and gender, calculate the mean age.
u7 = users.groupby(['occupation','gender']).agg(np.mean)
print("vii. Mean age", u7['age'])
# viii. Per occupation present the percentage of women and men.
t = lambda x: 100 * x / float(x.sum())

u8 = users.groupby(['occupation', 'gender']).agg({'gender': 'count'})
u8_perc = u8.groupby(level=0).apply(t)
print("viii. Percentages of women and men per occupation:")
print(u8_perc)
print('#',50*"-")
# ----------------------------------------------------------------
# Solution Class_Ex1: From the data table above, create an index to return all rows for
# which the phylum name ends in "bacteria" and the value is greater than 1000.
print("Solution Class_Ex1")
data = pd.DataFrame({'value':[632, 1638, 569, 115, 433, 1130, 754, 555],
                     'patient':[1, 1, 1, 1, 2, 2, 2, 2],
                     'phylum':['Firmicutes', 'Proteobacteria', 'Actinobacteria',
    'Bacteroidetes', 'Firmicutes', 'Proteobacteria', 'Actinobacteria', 'Bacteroidetes']})


print(data[data.phylum.str.endswith('bacteria') & (data.value > 1000)])
print('#',50*"-")

# ----------------------------------------------------------------
# Solution Clas_Ex2: Create a treatment column and add it to DataFrame that has 6 entries
# which the first 4 are zero and the 5 and 6 element are 1 the rest are NAN
print("Solution Class_Ex2")
df_ex2 = pd.DataFrame(np.nan, index=[0, 1, 2, 3, 4, 5, 6], columns=['A', 'B'])
df_ex2['treatment']=pd.Series([0, 0, 0, 0, 0, 1, 1])
print(df_ex2)
print('#',50*"-")

# ----------------------------------------------------------------
# Solution Class_Ex3:Create a month column and add it to DataFrame. Just for month Jan.
# Using data from Class_Ex2
print("Solution Class_Ex3")
data['month']=pd.Series("Jan")
print(data)
print('#',50*"-")

# ----------------------------------------------------------------
# Solution Class_Ex4: Drop the month column.
# Using data from Class_Ex2
print("Solution Class_Ex4")
data = data.drop(['month'], axis=1)
print(data)
print('#',50*"-")

# ----------------------------------------------------------------
# Solution Class_Ex5: Create a numpy array that has all teh values of DataFrame.
print("Solution Class_Ex5")
data_numpy = data.to_numpy()
print('#',50*"-")

# ----------------------------------------------------------------
# Solution Class_Ex6: Read baseball data into DataFrame and check the
# first and last 10 rows
print("Solution Class_Ex6")
baseball = pd.read_csv("baseball.csv" )
print(baseball.head(10))
print(baseball.tail(10))

print('#',50*"-")

# ----------------------------------------------------------------
# Solution Class_Ex7: Cretae a unique index by specifying the id column
# as the index. Check the new df and verify it is unique
print("Solution Class_Ex7")
df = baseball.set_index('id')
count = df.shape[0]
df.drop_duplicates
count_no_dups = df.shape[0]
if count == count_no_dups:
  print("Confirmed no duplicates in new df with id as index, # rows:", df.shape[0])
else:
  print("Not unique")

print('#',50*"-")

# ----------------------------------------------------------------
# Solution Class_ex8: Populate id column to be a sequence of numbers where Pandas
# fills in missing data with NaN values. Using df from previous step.
print("Solution Class_Ex8")
df.sort_index(inplace=True, ignore_index=True)
id_0 = df.index[0]
id_1 = df.index[-1]
print("first index", id_0)
print("last index", id_1)
df_ex8 = pd.DataFrame(df,index=range(id_0, id_1 + 1, 1))

print('#',50*"-")

# ----------------------------------------------------------------
# Solution Class_Ex9: Fill the missing values.  Filled with 0s.
print("Solution Class_Ex9")
df_ex8.fillna(0)
print(df_ex8)
print('#',50*"-")

# ----------------------------------------------------------------
# Solution Class_Ex10: Find the shape of the new df
print("Solution Class_Ex10")
print(df_ex8.shape)
print('#',50*"-")

# ----------------------------------------------------------------
# Solution Class_Ex11: Drop row 89525 and 89526
print("Solution Class_Ex11")
df_ex8 = df_ex8.drop(index= 89525)
df_ex8 = df_ex8.drop(index=89526)
print(df_ex8.tail(15))
print('#',50*"-")

# ----------------------------------------------------------------
# Solution Class_Ex12: sort the df descending and not ascending
print("Solution Class_Ex12")
df_ex8.sort_index(ascending=False)
print('#',50*"-")

