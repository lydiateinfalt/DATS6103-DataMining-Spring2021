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



