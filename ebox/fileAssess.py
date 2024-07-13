#Q1 
# Letter Frequency
# Prakash is the English school teacher at Aksh public school. He wants to teach the English characters to the 1st class students. After taking the class he wanted to know whether his students recognize the letters of English alphabet. So he gave his students a English sentence, and asked them to write down the count of each character in alphabatical order.
 
# Help the students to find the count by writing a program that builds a frequency listing of the characters contained in the file, and prints a sorted and formatted character frequency table to the screen.
 
# Note:
# Read the input from the file and print the output in the console.  
# Input File should be named as frequencyFile.txt.
 
# Input File Content:
# Set of words (or sentences).  
 
# Output Format:  
# Print a sorted and formatted character frequency table. 

# Sample Input and Output: 
# b: 1
# i: 1
# n: 2
# o: 2
# r: 1



from  collections import Counter

f =  open("frequencyFile.txt", "r")
content = f.read() # read all content from the file 

# remove all the unnecessary character like space and \n new line
content  = content.lower().replace(' ', '').replace('\n', '')

# count the frequency of character and store in dictionary
char_count = Counter(content)

# sort the items in the dictionary  
sort_char = sorted(char_count.items(), key=lambda items: items[0])
for  char,  count in  sort_char :
    print(f"{char}: {count}")


# Q2 
# Problem

# CSV write

# Saahil is working as a Receptionist at ABC Engineering College. The CSE department is conducting interview for the post of Asst. Professor. He was asked to note down the salary expectation of all the interviewees. Due to some error with MS Excel software and he is not able to write the details in the CSV format. So help him by writing a program that would write the given data to a file, and finally print the file content.

# Note :
# Read the input from the console and write the output to a file.

# The name of the output file should be "salaryData.csv".

# Input Format:
# First Line is an integer corresponding to 'n' the number of persons.
# next n*2 lines corresponds to each persons name and salary.

# Sample Input:
# 4
# nisha
# 30000
# karthikeyan
# 40000
# krishna
# 30000
# shakthi
# 35000

# Output File Format:
# nisha,30000
# karthikeyan,40000
# krishna,30000
# shakthi,35000

n = int(input())

data = []
for i in range(n):
    name = input().strip()
    salary = input().strip()
    data.append((name,salary))

f = open("salaryData.csv", "w")
for name,salary in data:
    f.write(f"{name},{salary}\n")