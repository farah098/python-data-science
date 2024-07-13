#Q1
# P4 / Index Error
# ===================
# An input list is given in the code template.
# Write a program to find the sum of first n values from the given list.
# For invalid ‘n’ values, raise an IndexError Exception and display the message shown in the sample output.
# Input and Output Format:
# Refer Sample Input and Output for formatting specifications.
# All text in bold corresponds to input and the rest corresponds to output.
# Sample Input and Output 1:
# [2, 3, 1, 5, 6, 7, 1]
# Enter n
# 5
# Sum = 17
# Sample Input and Output 2:
# [2, 3, 1, 5, 6, 7, 1]
# Enter n
# 10
# Index Value out of range

 
numlist = [2,3,1,5,6,7,1]
print(numlist)

n = int(input("Enter n\n"))
try:
    sum1 =0
    for i in range(n):
        sum1 += numlist[i]

    print(f"Sum = {sum1}")
except IndexError:
    print("Index Value out of range")

# Q2

username = input("Enter the username\n")
password = input("Enter the password\n")

class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
    
low = 0
up = 0
num = 0 

for i in password:
    if i.islower():
        low += 1
    if i.isupper():
        up += 1
    if i.isdecimal():
        num += 1

try:
    if low >= 1 and up >= 1 and num >= 1:
        print(f"Employee Username: {username} \n Password: {password}")
    else:
        raise CustomError
except : 
    print("CustomException: Invalid Password Exception")

