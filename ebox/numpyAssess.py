#Q1
'''Creating Ranges in numpy

Write a Python program to create 2 1-D arrays using arange function defined in numpy library.
1) Array with values between 0 and 100 (0 inclusive and 100 exclusive)
2) Array with all multiples of 100 between 2000 and 10000(2000 inclusive and 10000 exclusive)

Sample Output :
Array 1
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95
 96 97 98 99]
Array 2
[2000 2100 2200 2300 2400 2500 2600 2700 2800 2900 3000 3100 3200 3300
 3400 3500 3600 3700 3800 3900 4000 4100 4200 4300 4400 4500 4600 4700
 4800 4900 5000 5100 5200 5300 5400 5500 5600 5700 5800 5900 6000 6100
 6200 6300 6400 6500 6600 6700 6800 6900 7000 7100 7200 7300 7400 7500
 7600 7700 7800 7900 8000 8100 8200 8300 8400 8500 8600 8700 8800 8900
 9000 9100 9200 9300 9400 9500 9600 9700 9800 9900]'''

import numpy as np

# Create an array with values between 0 and 100 (0 inclusive, 100 exclusive)
arr1 = np.arange(0, 100)
print("Array 1")
print(arr1)

# Create an array with all multiples of 100 between 2000 and 10000 (2000 inclusive, 10000 exclusive)
arr2 = np.arange(2000, 10000, 100)
print("Array 2")
print(arr2)

#Q2
'''
Explore Iris Dataset

Write a Python program to explore the characteristics of a dataset . Let us use the iris dataset defined in the sklearn library. Print the following details about the Iris Dataset --- Feature names, Target Names, First 5 rows of the iris data and the first 5 rows of the iris target vector.

Refer the below link to get details about the iris dataset defined in sklearn library.
https://scikit-learn.org/0.16/modules/generated/sklearn.datasets.load_iris.html

Refer sample output for formatting specifications.

Iris dataset from the sklearn library is considered as the input.

Sample Output:

Iris Feature Names
['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
Iris Target Names
['setosa' 'versicolor' 'virginica']
Iris Feature Matrix
[[5.1 3.5 1.4 0.2]
 [4.9 3.  1.4 0.2]
 [4.7 3.2 1.3 0.2]
 [4.6 3.1 1.5 0.2]
 [5.  3.6 1.4 0.2]]
Iris Target Vector
[0 0 0 0 0]
Type of Iris Feature Matrix
class 'numpy.ndarray'
Type of Iris Target Vector
class 'numpy.ndarray'
'''
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()

# Extract the feature names, target names, data, and target
feature_names = iris.feature_names
target_names = iris.target_names
data = iris.data
target = iris.target

# Print the required details
print("Iris Feature Names")
print(feature_names)
print("Iris Target Names")
print(target_names)
print("Iris Feature Matrix")
print(data[:5])  # Print first 5 rows of the feature matrix
print("Iris Target Vector")
print(target[:5])  # Print first 5 rows of the target vector
print("Type of Iris Feature Matrix")
print(str(type(data)).replace('<', '').replace('>', ''))
print("Type of Iris Target Vector")
print(str(type(target)).replace('<', '').replace('>', ''))

