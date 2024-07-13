#Q1
'''Chebyshev distance - Similarity

In this problem, given two feature vectors as input , find the Chebyshev distance between the given vectors without using any inbuild python libraries.

Input format :
1st line of input is an integer ‘n’, which corresponds to the length of both the vectors
Next 2 lines of input consists of ‘n’ space separated integers, which corresponds to the 1st and 2nd input vectors .

Output Format :
Output corresponds to single integer value, which corresponds to the Chebyshev Distance between the vectors.

Note : print ‘Invalid Input’ , if the vectors length doesn’t match.

Sample Input :
Enter the length of the array
3
1 5 89
236 4 58

Sample Output :
235'''

def chebyshev_distance(vector1, vector2):
    if len(vector1) != len(vector2):
        return "Invalid Input"

    max_distance = 0
    for i in range(len(vector1)):
        distance = abs(vector1[i] - vector2[i])
        if distance > max_distance:
            max_distance = distance

    return max_distance

def main():
    # Reading input
    print("Enter the length of the array")
    n = int(input().strip())
    
    vector1 = list(map(int, input().strip().split()))
    vector2 = list(map(int, input().strip().split()))
    
    # Checking if the vectors have the same length
    if len(vector1) != n or len(vector2) != n:
        print("Invalid Input")
        return
    
    # Calculate Chebyshev distance
    distance = chebyshev_distance(vector1, vector2)
    
    # Output the result
    print(distance)

if __name__ == "__main__":
    main()

#Q2
'''
Mean-Std-Var-1

Write a python program to find the mean,std and var from pandas dataframe.

Input Format
Input is a file in CSV format.

Output Format
First line of output refers to mean of the column "pl"
Second line of output refers to variance of the column "pl"
Third line of output refers to standard deviation of the column "pl"

Use 2 precisions for float
Input File name-"iris.csv"

Sample Input
File Input(csv)

Sample Output

5.79 
0.64 
0.80
'''

import pandas as pd

def main():
    # Read the CSV file
    df = pd.read_csv("iris.csv")
    
    # Check if the 'pl' column exists
    if 'pl' not in df.columns:
        print("Column 'pl' not found in the CSV file.")
        return
    
    # Calculate mean, variance, and standard deviation
    mean_value = df['pl'].mean()
    variance_value = df['pl'].var()
    std_dev_value = df['pl'].std()

    # Print results with 2 decimal precision
    print(f"{mean_value:.2f}")
    print(f"{variance_value:.2f}")
    print(f"{std_dev_value:.2f}")

if __name__ == "__main__":
    main()

#Q3
'''
Mean-Std-Var-2

Write a python program to find the mean,std and var from pandas dataframe.

Input Format
Input is a file in CSV format.

Output Format
First line of output refers to mean of the column "cyl"
Second line of output refers to variance of the column "cyl"
Third line of output refers to standard deviation of the column "cyl"

Use 2 precisions for float
Input File name-"cars.csv"

Sample Input
File Input(csv)

Sample Output

6.50
2.40
1.55'''
import pandas as pd

# Read the CSV file
df = pd.read_csv("cars.csv")

# Check if the 'cyl' column exists
if 'cyl' not in df.columns:
    print("Column 'cyl' not found in the CSV file.")

# Calculate mean, variance, and standard deviation
mean_value = df['cyl'].mean()
variance_value = df['cyl'].var()
std_dev_value = df['cyl'].std()

# Print results with 2 decimal precision
print(f"{mean_value:.2f}")
print(f"{variance_value:.2f}")
print(f"{std_dev_value:.2f}")


