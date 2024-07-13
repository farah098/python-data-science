#Q1
'''Merge 2 Data Frames
Write a Python program to merge 2 Data Frames.
The 2 Data Frames to be merged are given as part of the template code
Print the First Data Frame
Print the Second Data Frame
Merge the 2 Data Frames and rearrange the columns in the order student_name , department , sem1_cgpa, sem2_cgpa
Print the entire contents of the merged Data Frame'''
#Merge DataFrames, Change column order

import pandas as pd

df1 = pd.DataFrame([["Anitha",7.8,8.9], ["Baskar",5.6,6.9]], columns = ["student_name","sem1_cgpa", "sem2_cgpa"])
df2 = pd.DataFrame([["Anitha","CSE"], ["Baskar","IT"]], columns = ["student_name","department"])

print("DataFrame1")
print(df1)

print("DataFrame2")
print(df2)


# Fill in the code here
print("Merged DataFrame")
merge_df = pd.merge(df1,df2, on = "student_name")
merge_df = merge_df[["student_name", "department", "sem1_cgpa", "sem2_cgpa"]]
print(merge_df)


#Q2
''' Remove Duplicates from a Data Frame
Write a Python program to rename a specific column in a Data Frame.
Import the given CSV file as a Data Frame.
Print the entire contents of the Data Frame
Remove the Duplicate Rows from the Data Frame
Print the entire contents of the Data Frame
The input file to be used is iris_duplicates.csv file. Note that there is a header row in the input file.
The input file is given as part of the template code.'''

import pandas as pd

print("Original DataFrame")
df = pd.read_csv("iris_duplicates.csv")
print(df)

print("DataFrame after removing duplicates")
df.drop_duplicates(inplace=True)
print(df)
