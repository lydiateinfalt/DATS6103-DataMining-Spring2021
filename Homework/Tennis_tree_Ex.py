# Lydia Teinfalt
# DATS 6103 Spring21
# 4/9/2021
# %%%%%%%%%%%%% Machine Learning %%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# Deepak Agarwal------>Email:deepakagarwal@gwmail.gwu.edu
# %%%%%%%%%%%%% Date:
# V1 June - 05 - 2018
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Decision Tree  %%%%%%%%%%%%%%%%%%%%%%%%%%
#%%-----------------------------------------------------------------------
#%%-----------------------------------------------------------------------
# Exercise
#%%-----------------------------------------------------------------------

# 1:
# Build the simple tennis table we just reviewed, in python as a dataframe. Label the columns.
# We are going to calculate entropy manually, but in python.
# Make sure to enter all variables as binary vs. the actual categorical names
# Name the dataframe tennis_ex.
#%%-----------------------------------------------------------------------
from math import log2
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.preprocessing import OneHotEncoder

data = ["sunny","hot","high", False, "no"]
data1 = ["sunny","hot","high", True, "no"]
data2 = ["overcast","hot","high", False, "yes"]
data3 = ["rainy","mild","high", False, "yes"]
data4 = ["rainy","cool","normal", False, "yes"]
data5 = ["rainy","cool","normal", True, "no"]
data6 = ["overcast","cool","normal", True, "yes"]
data7 = ["sunny","mild","high", False, "no"]
data8 = ["sunny","cool","normal", False, "yes"]
data9 = ["rainy","mild","normal", False, "yes"]
data10 = ["sunny","mild","normal", True, "yes"]
data11 = ["overcast","mild","high", True, "yes"]
data12 = ["overcast","hot","normal", False, "yes"]
data13 = ["rainy","mild","high", True, "no"]
dx = [data, data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13]

feature_cols = ['outlook', 'temp', 'humidity', 'windy']
#tennis = pd.read_csv('tennis.csv')
#creating panda dataframe based on the last slide in professor's lecture 8
tennis_ex = pd.DataFrame(dx, columns = ['outlook', 'temp', 'humidity', 'windy', 'play'])
print("Before encoding")
print(tennis_ex)

# Create independent variables using outlook, temp, humidity and windy columns from the df
# Target is play
X = tennis_ex[['outlook', 'temp', 'humidity', 'windy']]
y = tennis_ex[['play']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 100)

# Using OneHotEncoder to convert categorical variables in X as in binary variables (0 or 1)
ohe = OneHotEncoder()

ohe.fit(X_train)
X_train_ohe = ohe.transform(X_train).toarray()

ohe_df = pd.DataFrame(X_train_ohe, columns=ohe.get_feature_names(X_train.columns))
# update feature columns so we can use in the graphical user interface representation later
feature_cols = ohe_df.columns.tolist()
print(ohe_df.head())
#%%-----------------------------------------------------------------------

# printing the dataset shape
print ('-'*40 + 'Start Console' + '-'*40 + '\n')

print("Dataset No. of Rows: ", ohe_df.shape[0])
print("Dataset No. of Columns: ", ohe_df.shape[1])

# printing the dataset observations
print("Dataset first few rows:\n ")
print(ohe_df.head())

print ('-'*80 + '\n')

# printing the structure of the dataset
print("Dataset info:\n ")
print(ohe_df.info())
print ('-'*80 + '\n')
# printing the summary statistics of the dataset
print(ohe_df.describe(include='all'))
print ('-'*80 + '\n')
#%%-----------------------------------------------------------------------

#%%-----------------------------------------------------------------------
# 2:
# Build a function that will calculate entropy. Calculate entropy for the table we just went over
# in the example, but in python
# This is for the first split.
#%%-----------------------------------------------------------------------

# For calculating, using original dataframe
#my function for calculating entropy
def entropyx(n,m):
    total = n + m
    if n == 0:
        return 0.0
    elif m == 0:
        return 0.0
    else:
        return -((n/total)*log2(n/total)) - ((m/total)*log2(m/total))

#Entropy function from: https://www.coursehero.com/tutors-problems/Python-Programming/26709067-def-entropyApproval-elementscountsnpuniqueApprovalreturncount/
def entropy(feature):
  elements,counts=np.unique(feature,return_counts=True)
  entropy=np.sum([(-counts[i]/np.sum(counts))*np.log2(counts[i]/np.sum(counts))for i in range(len(elements))])
  return entropy

#entropy(playing tennis)
n0, n1 = tennis_ex['play'].value_counts()
total_entropy= entropyx(n0, n1)
print("Total Entropy for playing tennis using my function",total_entropy)
print("Total Entropy for playing tennis using borrowed function",entropy(tennis_ex.play))

#entropy(playing tennis, outlook)
ns = tennis_ex[(tennis_ex['outlook'] == 'sunny')]['outlook'].count()
nr = tennis_ex[(tennis_ex['outlook'] == 'rainy')]['outlook'].count()
no = tennis_ex[(tennis_ex['outlook'] == 'overcast')]['outlook'].count()
#print(ns, nr, no)
total = ns + nr + no
ent1 = entropyx(2,3)
ent2 = entropyx(4,0)
ent3 = entropyx(3,2)
#this was giving me a warning
#ent = (ns/total)*ent1 +(no/total)*ent2 + (nr/total)*ent3
#info_gain = total_entropy - ent

print("Entropy for temp", entropy(tennis_ex.temp))
print("Entropy for humidity", entropy(tennis_ex.humidity))
print("Entropy for wind", entropy(tennis_ex.windy))


def InfoGain (raw,feature,target_name="play"):
 total_entropy = entropy(raw[target_name])
 vals,counts= np.unique(raw[feature],return_counts=True)
 Weighted_Entropy = np.sum([(counts[i]/np.sum(counts))*entropy(tennis_ex.where(tennis_ex[feature]==vals[i]).dropna()[target_name]) for i in range(len(vals))])
 # print("Weighted entropy of {} is {}".format(feature,Weighted_Entropy))
 InfoGain = total_entropy - Weighted_Entropy
 print("Information gain of {} is {}".format(feature,InfoGain))
 return InfoGain

#Calculate information gain for each feature column
for feature in tennis_ex.columns:
    target= 'play'
    dict ={}
    if feature != target:
        ig = InfoGain(tennis_ex, feature, target)
        dict[feature] = ig
    print(dict)

print("Weather 'outlook' has the highest information gain and entropy value of", entropy('outlook'))

#%%-----------------------------------------------------------------------
# 3:
# Run the decision tree algorithm and find out the best feature and graph it.
#%%-----------------------------------------------------------------------

# perform training with giniIndex.
# creating the classifier object
clf_gini = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=3, min_samples_leaf=2)

# performing training using encoded X training split
clf_gini.fit(X_train_ohe, y_train)

# perform training with entropy.
# Decision tree with entropy
clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=100, max_depth=3, min_samples_leaf=2)

# Performing training
clf_entropy.fit(X_train_ohe, y_train)
print("Text Tree Entropy")
text_representation_entropy = tree.export_text(clf_entropy)
print(text_representation_entropy)

# entropy
fig, axes = plt.subplots(nrows = 1,ncols = 1, figsize = (3,3), dpi=300)
tree.plot_tree(clf_entropy,
               feature_names = ohe_df.columns,
               class_names=np.unique(y).astype('str'),
               filled = True)
plt.show()

# gini
fig, axes = plt.subplots(nrows = 1,ncols = 1, figsize = (3,3), dpi=300)
tree.plot_tree(clf_gini,
               feature_names = ohe_df.columns,
               class_names=np.unique(y).astype('str'),
               filled = True)
plt.show()

# make predictions
# predicton on test using gini
X_test_ohe = ohe.transform(X_test)

y_pred_gini = clf_gini.predict(X_test_ohe)

# prediction on test using entropy
y_pred_entropy = clf_entropy.predict(X_test_ohe)
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

#%%-----------------------------------------------------------------------
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
#%%-----------------------------------------------------------------------

# Libraries to display decision tree
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz
import webbrowser
#%%--------------------------------Save Console----------------------------

# old_stdout = sys.stdout
# log_file = open("console.txt", "w")
# sys.stdout = log_file

#%%-----------------------------------------------------------------------

# confusion matrix for gini model
conf_matrix = confusion_matrix(y_test, y_pred_gini)
class_names = tennis_ex.play.unique()
df_cm = pd.DataFrame(conf_matrix, index=class_names, columns=class_names)

plt.figure(figsize=(5,5))
hm = sns.heatmap(df_cm, cbar=False, annot=True, square=True, fmt='d', annot_kws={'size': 20}, yticklabels=df_cm.columns, xticklabels=df_cm.columns)
hm.yaxis.set_ticklabels(hm.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
hm.xaxis.set_ticklabels(hm.xaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
plt.ylabel('True label',fontsize=20)
plt.xlabel('Predicted label',fontsize=20)
plt.tight_layout()
plt.show()

#%%-----------------------------------------------------------------------

# confusion matrix for entropy model
conf_matrix = confusion_matrix(y_test, y_pred_entropy)
class_names = tennis_ex.play.unique()
df_cm = pd.DataFrame(conf_matrix, index=class_names, columns=class_names )

plt.figure(figsize=(5,5))
hm = sns.heatmap(df_cm, cbar=False, annot=True, square=True, fmt='d', annot_kws={'size': 20}, yticklabels=df_cm.columns, xticklabels=df_cm.columns)
hm.yaxis.set_ticklabels(hm.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
hm.xaxis.set_ticklabels(hm.xaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
plt.ylabel('True label',fontsize=20)
plt.xlabel('Predicted label',fontsize=20)
plt.tight_layout()
plt.show()

#%%-----------------------------------------------------------------------
# display decision tree
dot_data = export_graphviz(clf_gini, filled=True, rounded=True, class_names=class_names , feature_names=feature_cols, out_file=None)

graph = graph_from_dot_data(dot_data)
graph.write_pdf("decision_tree_gini_tennis.pdf")
webbrowser.open_new(r'decision_tree_gini_tennis.pdf')

#%%-----------------------------------------------------------------------
# display decision tree

dot_data = export_graphviz(clf_entropy, filled=True, rounded=True, class_names=class_names, feature_names=feature_cols, out_file=None)

graph = graph_from_dot_data(dot_data)
graph.write_pdf("decision_tree_entropy_tennis.pdf")
webbrowser.open_new(r'decision_tree_entropy_tennis.pdf')

print ('-'*40 + 'End Console' + '-'*40 + '\n')
