# %%%%%%%%%%%%% Machine Learning %%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# Deepak Agarwal------>Email:deepakagarwal@gwmail.gwu.edu
# %%%%%%%%%%%%% Date:
# V1 June - 05 - 2018
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Decision Tree  %%%%%%%%%%%%%%%%%%%%%%%%%%
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import tree
import warnings
warnings.filterwarnings("ignore")
import sys
#%%-----------------------------------------------------------------------
import os
os.environ["PATH"] += os.pathsep + 'C:\Program Files (x86)\Graphviz\bin'
#%%-----------------------------------------------------------------------

# Libraries to display decision tree
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz
import webbrowser
#%%--------------------------------Save Console----------------------------


#%%-----------------------------------------------------------------------
# Exercise
#%%-----------------------------------------------------------------------
# Specify what are your features and targets. Why this is a classification
# 1- Use the bank banknote dataset.
# 2- Specify what are your features and targets.
# 3- Why this is a classification problem.
# 4- Run the decision tree algorithm.
# 5- Explain your findings and write down a paragraph to explain all the results.
#%%-----------------------------------------------------------------------
# importing Dataset
# 1-
# read data as panda dataframe

data = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/00267/' + 'data_banknote_authentication.txt', sep=',', header=None)

#%%-----------------------------------------------------------------------
# 2-Features
print("Features: variance of Wavelet Transformed image, skewness of Wavelet Transformed image, curtosis of Wavelet Transformed image, entropy of image")
data.columns = ['variance', 'skewness', 'curtosis', 'entropy', 'class']

feature_cols = ['variance', 'skewness', 'curtosis', 'entropy']
print("Features columns:", feature_cols)
# Target: Class
print("Target: Class (Forgery or not)")

#%%-----------------------------------------------------------------------
# 3- Why this is a classification problem.
print("This is a classification problem to predict if a bank note as real or a forgery.")

# printing the dataset shape
print ('-'*40 + 'Start Console' + '-'*40 + '\n')

print("Dataset No. of Rows: ", data.shape[0])
print("Dataset No. of Columns: ", data.shape[1])

# printing the dataset observations
print("Dataset first few rows:\n ")
print(data.head())

print ('-'*80 + '\n')

# printing the structure of the dataset
print("Dataset info:\n ")
print(data.info())
print ('-'*80 + '\n')
# printing the summary statistics of the dataset
print(data.describe(include='all'))
print ('-'*80 + '\n')
#%%-----------------------------------------------------------------------
# 4-
# split the dataset
# separate the target variable
X = data.values[:, 0:4]
y = data.values[:, 4]

# encloding the class with sklearn's LabelEncoder
class_le = LabelEncoder()

# fit and transform the class
y = class_le.fit_transform(y)

# split the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
#%%-----------------------------------------------------------------------
# perform training with giniIndex.
# creating the classifier object
clf_gini = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=3, min_samples_leaf=5)

# performing training
clf_gini.fit(X_train, y_train)
print("Text Tree Gini")
text_representation_gini = tree.export_text(clf_gini)
print(text_representation_gini)
#%%-----------------------------------------------------------------------
# perform training with entropy.
# Decision tree with entropy
clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=100, max_depth=3, min_samples_leaf=5)

# Performing training
clf_entropy.fit(X_train, y_train)
print("Text Tree Entropy")
text_representation_entropy = tree.export_text(clf_entropy)
print(text_representation_entropy)

#%%-----------------------------------------------------------------------
# make predictions
# prediction on test using gini
y_pred_gini = clf_gini.predict(X_test)

# predicton on test using entropy
y_pred_entropy = clf_entropy.predict(X_test)
#%%-----------------------------------------------------------------------
# calculate metrics gini model
print("\n")
print("Results Using Gini Index: \n")
print("Classification Report: ")
print(classification_report(y_test,y_pred_gini))
print("\n")
print("Accuracy : ", accuracy_score(y_test, y_pred_gini) * 100)
print("\n")
print ('-'*80 + '\n')
# calculate metrics entropy model
print("\n")
print("Results Using Entropy: \n")
print("Classification Report: ")
print(classification_report(y_test,y_pred_entropy))
print("\n")
print("Accuracy : ", accuracy_score(y_test, y_pred_entropy) * 100)
print ('-'*80 + '\n')


# confusion matrix for gini model
conf_matrix = confusion_matrix(y_test, y_pred_gini)
print("Gini Confusion Matrix")
print(confusion_matrix(y_test, y_pred_gini))
class_names = data['class'].unique()
df_cm = pd.DataFrame(conf_matrix, index=class_names, columns=class_names)

plt.figure(figsize=(5,5))
hm = sns.heatmap(df_cm, cbar=False, annot=True, square=True, fmt='d', annot_kws={'size': 20}, yticklabels=df_cm.columns, xticklabels=df_cm.columns)
hm.yaxis.set_ticklabels(hm.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
hm.xaxis.set_ticklabels(hm.xaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
plt.ylabel('True label',fontsize=20)
plt.xlabel('Predicted label',fontsize=20)
plt.title("Confusion Matrix using Gini")
plt.tight_layout()
plt.show()

#%%-----------------------------------------------------------------------

# confusion matrix for entropy model
conf_matrix = confusion_matrix(y_test, y_pred_entropy)
print("Entropy Confusion Matrix")
print(confusion_matrix(y_test, y_pred_entropy))
class_names = data['class'].unique()
df_cm = pd.DataFrame(conf_matrix, index=class_names, columns=class_names )

plt.figure(figsize=(5,5))
hm = sns.heatmap(df_cm, cbar=False, annot=True, square=True, fmt='d', annot_kws={'size': 20}, yticklabels=df_cm.columns, xticklabels=df_cm.columns)
hm.yaxis.set_ticklabels(hm.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
hm.xaxis.set_ticklabels(hm.xaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
plt.ylabel('True label',fontsize=20)
plt.xlabel('Predicted label',fontsize=20)
plt.title("Confusion Matrix using Entropy")
plt.tight_layout()
plt.show()

#%%-----------------------------------------------------------------------
# display decision tree
# display decision tree
#dot_data = export_graphviz(clf_gini, filled=True, rounded=True, class_names=["0", "1"], feature_names=['variance', 'skewness', 'curtosis', 'entropy'], out_file=None)
dot_data = export_graphviz(clf_gini, filled=True, rounded=True, class_names=["0", "1"], feature_names=data.iloc[:, 0:4].columns, out_file=None)

graph = graph_from_dot_data(dot_data)
graph.write_pdf("decision_tree_gini_ex.pdf")
webbrowser.open_new(r'decision_tree_gini_ex.pdf')

#%%-----------------------------------------------------------------------
# display decision tree

dot_data = export_graphviz(clf_entropy, filled=True, rounded=True, class_names=["0", "1"], feature_names=data.iloc[:, 0:4].columns, out_file=None)

graph = graph_from_dot_data(dot_data)
graph.write_pdf("decision_tree_entropy_ex.pdf")
webbrowser.open_new(r'decision_tree_entropy_ex.pdf')

print ('-'*40 + 'End Console' + '-'*40 + '\n')
#%%-----------------------------------------------------------------------
# 5-

print("The data set contains data about of bank notes.  We will be approaching this as a classification problem to determine if a bank is real or a forgery.")
print("The data contains 1372 observations with 5 columns.  The target is 'class' where 0 is a forgery and 1 is real bank note.")
print("The independent variables are: variance, skewness, curtosis, entropy. Here is a few sample rows of data", print(data.head()))
print("We split data between training and test at 30% and ran the Decision Tree Classifier algorithm.")
print("We asked the Decision Tree to run using Gini and Entropy models and make predictions.")
print("The Gini classification is 94% accurate.")
print("The Gini Model Confusion Matrix tells us it only misclassified 23.")
print(confusion_matrix(y_test, y_pred_gini))
print("The Entropy classification is slightly better than Gini with 95% accuracy.")
print(confusion_matrix(y_test, y_pred_entropy))
print("The Entropy Confusion Matrix tells us that it only misclassified 18.")
print("The visualization of decision tree, would be able to help us classify the data and predict.")
print("by anwering a series of questions. The feature that provided the highest information gain the entropy model")
print("is variance.  With the root node testing if variance is <= 0.76 and if that's true, it checks on skewness.")
print("In the gini model, the feature with the lowest Gini index is also variance is <=0.32. The second")
print("feature with next lowest index is skewness <= 7.565.")