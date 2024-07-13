#Q1
'''Create DF from List of Lists
Write a Python program to create a Pandas Data Frame from a List of Lists and print the Data Frame.
List of Lists is specified as part of the template code.
Refer Sample Output for formatting specifications.'''

import pandas as pd

data = [[5.1,3.5,1.4,0.2,"IrisSentosa"],
	[4.9,3.0,1.4,0.2,"IrisSentosa"],
	[4.9,3.0,1.4,0.2,"IrisVersicolor"],
	[6.4,3.2,4.5,1.5,"IrisVersicolor"],
	[6.3,3.3,6.0,2.5,"IrisVirginica"],
	[5.8,2.7,5.1,1.9,"IrisVirginica"]]

#Fill in the code here

columns = ['sepal_length','sepal_width', 'petal_length', 'petal_width', 'species_type']

df = pd.DataFrame(data,columns = columns)
print(df)


#Q2
'''Write a Python program to import the given CSV file as a Pandas Data Frame.
The input file to be used is iris.csv file. Note that there is no header row in the input file.
The input file is given as part of the template code.
Refer Sample Output for formatting specifications.'''

import pandas as pd 

columns = ['sepal_length','sepal_width', 'petal_length', 'petal_width', 'species_type']

df = pd.read_csv('iris.csv', header=None, names = columns, skiprows = 1)
print(df.to_string())

#Q3
'''Write a Python program to import specific columns from a given CSV file as a Pandas Data Frame.
The 2 columns to be imported are sepal_length and sepal_width.
The input file to be used is iris_with_header.csv file. Note that there is a header row in the input file.
The input file is given as part of the template code.
Refer Sample Output for formatting specifications.'''

import pandas as pd 

df = pd.read_csv('iris_with_header.csv')

specific_column = pd.DataFrame(df[['sepal_length', 'sepal_width']])
print(specific_column)
 