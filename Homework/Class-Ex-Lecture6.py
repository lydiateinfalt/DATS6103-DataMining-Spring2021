# =================================================================
# Class_Ex1:
# We will do some  manipulations on numpy arrays by importing some
# images of a racoon.
# scipy provides a 2D array of this image
# Plot the grey scale image of the racoon by using matplotlib
# ----------------------------------------------------------------
from scipy import misc
from scipy import optimize
from scipy import sparse
from scipy.sparse.linalg import spsolve
from scipy.optimize import fsolve
from scipy import linalg
from scipy import stats
from scipy import interpolate
from scipy.interpolate import interp1d
from scipy.stats import norm
from scipy.stats import rv_histogram


import matplotlib.pyplot as plt
face = misc.face(gray=True) ## Modify the face function

plt.gray()
plt.imshow(face)
plt.show()


print('#',50*"-")
# =================================================================
# Class_Ex2:
# If still the face is gray choose the color map function and make it
# gray
# ----------------------------------------------------------------

plt.imshow(face, plt.cm.gray)
plt.show()

print('#',50*"-")
# =================================================================
# Class_Ex3:
# Crop the image (an array of the image) with a narrower centering
# Plot the crop image again.
# ----------------------------------------------------------------

face1=face[0:550, 300:1000]
plt.imshow(face1)
plt.show()

print('#',50*"-")
# =================================================================
# Class_Ex4:
# Take the racoon face out and mask everything with black color.
# ----------------------------------------------------------------

face4 = face
face4[500:774, 0:1024] = 0
face4[0:550, 0:350] = 0
plt.imshow(face4)
plt.show()

print('#',50*"-")
# =================================================================
# Solution Class_Ex5: For linear equation systems on the matrix form Ax=b where A is
# a matrix and x,b are vectors use scipy to solve the for x.
# ----------------------------------------------------------------
import numpy as np
print("Solution to Class_Ex5")
A = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
B = np.array([[2, 0], [-1, 0], [2, 0]])
x = spsolve(A, B)
print(x)
print('#',50*"-")
# =================================================================
# Solution Class_Ex6: # Calculate eigenvalue of matrix A. (create any matrix and check your # results.)
# Reference: https://www.math.ubc.ca/~pwalls/math-python/linear-algebra/eigenvalues-eigenvectors/
# ----------------------------------------------------------------
print("Solution to Class_Ex6")
A = np.array([[0,1],[-2, -3]])
ex6 = linalg.eigvals(A)
B = np.array([[1,2,3],[4,5,6]])
print(ex6)

print('#',50*"-")
# =================================================================
# Class_Ex7:
# Sparse matrices are often useful in numerical simulations dealing
# with large datasets. Convert sparse matrix to dense and vice versa
# ----------------------------------------------------------------
# Reference: https://machinelearningmastery.com/sparse-matrices-for-machine-learning/

print("Solution to Class_Ex7")
A = np.array([[1,0,0,0,1,0],[0,0,2,0,0,1],[0,0,0,0,0,1]])
S = sparse.csr_matrix(A)
print(S)
# reconstruct dense matrix
B = S.todense()
print(B)
print('#',50*"-")

# =================================================================
# Solution Class_Ex8: Create any polynomial to order of 3 and write python function for it
# then use scipy to minimize the function (use Scipy)
# ----------------------------------------------------------------

import matplotlib.pyplot as plt1
# Reference https://realpython.com/python-scipy-cluster-optimize/#minimizing-a-function-with-one-variable
print("Solution for Class_Ex8: 4 * x ** 3 - 2 * x + 1")
def p(x):
    return 4 * x ** 3 - 2 * x + 1

for x in [-2,0,2,3]:
    print(x,p(x))

x = np.linspace(-1, 1,num=10)
fx = []

for i in range(len(x)):
    fx.append(p(x[i]))
plt1.plot(x,fx)
plt1.xlabel("x")
plt1.ylabel("f(x)")
plt1.title("f(x) = 4 * x ** 3 - 2 * x + 1")
plt1.show()
result = optimize.minimize_scalar(p, method='bounded', bounds=(-1, 1))
print("Used SciPy minimize_scalar to minimize function:",result.success)

print('#',50*"-")
# =================================================================
# Class_Ex9:
# use the brent or fminbound functions for optimization and try again.
# (use Scipy)
# ----------------------------------------------------------------

print("Solution Class_Ex9")
result = optimize.minimize_scalar(p, method="Brent", bracket=(0,0.5))
print("Using Brent method")
print(result)
print("Used SciPy minimize_scalar to minimize function:",result.success)
print("Using fmindbound (-1, 1)")
minimum = optimize.fminbound(p, -1, 1)
print(minimum)

print('#',50*"-")
# =================================================================
# Class_Ex10:
# Find a solution to a function. f(x)=0 use the fsolve (use Scipy)
# ----------------------------------------------------------------
# Reference https://www.kite.com/python/examples/1011/scipy-find-the-roots-of-a-function

def func(x):
    return x**2 - 1
print(fsolve(func, 1))


print('#',50*"-")
# =================================================================
# Class_Ex11:
# Create a sine or cosine function with a big step size. Use scipy to
# interpolate between each data points. Use different interpolations.
# plot the results (use Scipy)
# ----------------------------------------------------------------
# Referemce https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html

x = np.linspace(0, 4*np.pi, 10)
y = np.sin(x)
splines = interpolate.splrep(x, y)
new_x = np.linspace(0, 4*np.pi, 50)
new_y = interpolate.splev(new_x, splines)
plt.plot(x, y, 'o') # plot known data points
plt.plot(new_x, new_y, '-x') # plot interpolated points
plt.show()

x = np.linspace(0, 10, num=11)
y = np.cos(-x**2/9.0)
f = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')

x1 = np.linspace(0, 10, num=41)
plt.plot(x, y, 'o', x1, f(x1), '-', x1, f2(x1), '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()

print('#',50*"-")
# =================================================================
# Class_Ex12:
# Use scipy statistics methods on randomly created array (use Scipy)
# PDF, CDF (CUMsum), Mean, Std, Histogram
# ----------------------------------------------------------------


array = np.random.randn(100)
norm_cdf = norm.cdf(array)
norm_pdf = norm.pdf(array)
print(norm_cdf)
print(norm_pdf)
mean = norm.mean(array)
std = norm.std(array)
print(mean)
print(std)
hist = np.histogram(array, bins=10)
print(hist)

print('#',50*"-")
# =================================================================
# Class_Ex13:
# USe hypothesise testing  if two datasets of (independent) random variables
# comes from the same distribution (use Scipy)
# Calculate p values.
# ----------------------------------------------------------------






print('#',50*"-")
# ----------------------------------------------------------------