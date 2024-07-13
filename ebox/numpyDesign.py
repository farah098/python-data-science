#Q1
'''Read from csv file

Write a python program to read from a csv file into a numpy array. Print the array.
The name of the input csv file is sample_data.csv. It is provided as part of the template code.

Refer sample input and output for formatting specifications.

Sample Input:

File Input. (sample_data.csv)

Sample Output:

[['Username' 'Identifier' 'First name' 'Last name']
 ['booker12' '9012' 'Rachel' 'Booker']
 ['grey07' '2070' 'Laura' 'Grey']
 ['johnson81' '4081' 'Craig' 'Johnson']
 ['jenkins46' '9346' 'Mary' 'Jenkins']
 ['smith79' '5079' 'Jamie' 'Smith']]'''

import pandas as pd 
import numpy as np

df = pd.read_csv('sample_data.csv', header =None)

data_array = df.to_numpy()

print(data_array)


#Q2
'''
Initalize Numpy Array

Write a python program to initialize a numpy array with values [1,2,3,4,5,6,7,8,9,10] and print the array and its type.

Refer sample output for fomatting specifications.

Sample Output:

Array
[ 1  2  3  4  5  6  7  8  9 10]
Array Type
class 'numpy.ndarray'
'''

import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10])

print("Array")
print(array)

print("Array Type")
print(str(type(array)).replace('<', '').replace('>', ''))
