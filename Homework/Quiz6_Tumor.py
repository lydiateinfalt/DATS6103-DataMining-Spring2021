# Quiz 6 Lydia Teinfalt
# DATS 6103 Spring 2021
# Reference: https://machinelearningmastery.com/implement-simple-linear-regression-scratch-python/
import pandas as pd
import matplotlib.pyplot as plt
col_names = ["Gender","Age Range","Tumor Size(cm^3)", "Weight(grams)"]
tumor = pd.read_csv("Tumor.csv", header=0, names=col_names)


# printing the dataset shape
print("Dataset No. of Rows: ", tumor.shape[0])
print("Dataset No. of Columns: ", tumor.shape[1])

# printing the dataset observations
print("Dataset first few rows:\n ")
print(tumor.head(2))

# printing the struture of the dataset
print("Dataset info:\n ")
print(tumor.info())

# printing the summary statistics of the dataset
print(tumor.describe(include='all'))

tumor.rename(columns={'Tumor Size(cm^3)': 'Tumor Size', 'Weight(grams)': 'Weight'}, inplace=True)
x = tumor['Tumor Size']
y = tumor['Weight']

# Estimate Mean and Variance

# Calculate the mean value of a list of numbers
def mean(values):
    return sum(values) / float(len(values))


# Calculate the variance of a list of numbers
def variance(values, mean):
    return sum([(x - mean) ** 2 for x in values])


# calculate mean and variance

mean_x, mean_y = mean(x), mean(y)
var_x, var_y = variance(x, mean_x), variance(y, mean_y)
print('x stats: mean=%.3f variance=%.3f' % (mean_x, var_x))
print('y stats: mean=%.3f variance=%.3f' % (mean_y, var_y))

# Calculate Covariance

# Calculate the mean value of a list of numbers
def mean(values):
    return sum(values) / float(len(values))


# Calculate covariance between x and y
def covariance(x, mean_x, y, mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)
    return covar


# calculate covariance
mean_x, mean_y = mean(x), mean(y)
covar = covariance(x, mean_x, y, mean_y)
print('Covariance: %.3f' % (covar))


def mean(values):
	return sum(values) / float(len(values))

# Calculate covariance between x and y
def covariance(x, mean_x, y, mean_y):
	covar = 0.0
	for i in range(len(x)):
		covar += (x[i] - mean_x) * (y[i] - mean_y)
	return covar

# Calculate the variance of a list of numbers
def variance(values, mean):
	return sum([(x-mean)**2 for x in values])

plt.plot(x, y, 'o', color='blue');


# Calculate coefficients
def coefficients(dataset):
	x = [row[0] for row in dataset]
	y = [row[1] for row in dataset]
	x_mean = mean(x)
	y_mean = mean(y)
	b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
	b0 = y_mean - b1 * x_mean
	return [b0, b1]

# calculate coefficients
x_mean = mean(x)
y_mean = mean(y)
b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
b0 = y_mean - b1 * x_mean
print('Coefficients: B0=%.3f, B1=%.3f' % (b0, b1))
y_pred = b0+ b1*x
print(y_pred)
plt.plot(x, y_pred, 'o', color='orange');
plt.show()
