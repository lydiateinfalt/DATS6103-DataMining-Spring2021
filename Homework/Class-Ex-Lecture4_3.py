# =================================================================
# # Lydia Teinfalt
# # DATS 6103: Data Mining
# # Spring 2021
# # 02/26/2021
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

print("Joint plot shows both distribution of passenger ages and cost of fares.")
print("Distribution plot of fare prices against normal distribution.")
print("Box plots showed the age of passengers in first, second and third class.")
print("Swarm plots")
print("Count plots of passenger ages in first, second and third classes.")
print("Heat map showing correlation between factors in the titantic data set.")
print("Two histogram showing number of male and female passengers into one plot (using facet).")



