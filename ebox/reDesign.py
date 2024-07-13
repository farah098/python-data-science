#Q1
'''Password Extraction

Ebox Engineering college has lot of systems in various labs and libraries. Each system in college running with windows OS having different username with different passwords . Student can choose any non admin user from the system and have to extract password from the given hint. Password is always a number of any length or no password . From the hint given , user has to extract the maximum number and that extracted number will be used as password. If no number present in the hint then there is no password for that particular system user.

Help the students to find the password by writing a program.

Input and Output Format:

Input is single line string which is a hint. String contains only alphanumeric characters.

Output is a maximum number extracted from the input string.consider only positive numbers.print “No Password” without quotes when input has no number.

Refer sample input and output for formatting specifications

Sample Input 1:
hello123 abcd456 efgh99999
Sample Output 1:
99999

Sample Input 2:
abcdefgh
Sample Output 2:
No Password'''

import re

def extract_max_number(n):
    # Use regular expression to find all sequences of digits
    numbers = re.findall(r'\d+', n)
    
    # If no numbers found, return "No Password"
    if not numbers:
        return "No Password"
    
    # Convert all found numbers to integers
    numbers = [int(num) for num in numbers]
    
    # Return the maximum number as a string
    return str(max(numbers))

# Input
n = input(" ")

# Output
print(extract_max_number(n))

#Q2
'''Swiggy Special Offer Code
Swiggy is an online food ordering and delivery platform. For Holi festival they planned to give special offer upto 50% based on offer code shared by the Swiggy team. Due to lot of offer code forgery they set a pattern to create an offer code. The pattern for offer code was , it should be a word which contains all vowels. If there is any word without all vowels then that offer code was rejected by the swiggy team.
 
Input and Output Format:
Input is a string .Only lower case allowed.
Output is a string . Print “Accepted “ if offer code is valid else “Not Accepted” without quotes.
Refer sample input and output for formatting specifications.


Sample Input 1:
tragedious
Sample Output 1:
Accepted

Sample Input 2:
hello everyone
Sample Output 2:
Not Accepted'''

def check_offer_code(offer_code):
    # Define a set of all vowels
    vowels = set("aeiou")
    
    # Create a set from the input string to get unique characters
    unique_chars = set(offer_code)
    
    # Check if all vowels are in the unique characters of the input string
    if vowels.issubset(unique_chars):
        return "Accepted"
    else:
        return "Not Accepted"

# Input
offer_code = input()

# Output
print(check_offer_code(offer_code))


#Q3
'''
Block Spam Calls
 
In the digital world, it's easy to access contact details of individuals through online. Users give permission to third party apps to access basic details making it easy for spammers to get more contacts. Hackers are using this contact numbers for making Spam calls (irrelevant or inappropriate call sent over the phone) to annoy the users. So to handle this issue Cyber Crime Department need to analyze the valid and spam call mobile number pattern. The valid phone number pattern should contain following things:
1. It should start with "+91-" 
2. Followed by ten digits
If any mobile number violating the above rules can be blocked immediatley.

Input and Output Format:
Input is a string .
Output is a string . Refer sample input and output for formatting specifications.
 
Sample input 1:
+91-9876543210
Sample output 1:
Not a Spam Call
Sample input 2:
9876543210
Sample output 2:
Spam Call'''

import re

def spam_check(num):
    
    # re  pattern for valid phone number
    pattern = r"^\+91-\d{10}$"

    #condition to check if it is spam number or valid number
    if re.match(pattern, num):
        return "Not a Spam Call"
    else:
        return "Spam Call"

num = input()

print(spam_check(num))


#Q4
'''
String Shuffling Pattern
Jack and Daniel are two army officers deployed in one under cover operation inside terrorist camp. They follow certain encryption strategy to communicate each other inside the camp . They follow string shuffling pattern as their encryption strategy. In this strategy, they can pass any message of any length, but only two words allowed. From that two words they need to find encrypted string which is a single word. Encryption principle followed here is to join first character of first word and last character of second word,then second character of first word and second last character of second string and so on to form a encrypted string. If there is no enough characters in any of string , add remaining characters in other string in encrypted string. 
Help the officers to automate the process by writing a program.
Note:
No need to consider the decryption process.
Input and Output Format:
Input consists of two strings and output is a shuffled string which is a encrypted string. Refer sample input and output for formatting specifications.
Sample input:
hello
hi
Sample output:
hiehllo'''
# method 1
def shuffling(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    min_len = min(len1, len2)

    # Store the result of encrypted string
    encryptedS = []
    
    # Shuffling characters per given strategy
    for i in range(min_len):
        encryptedS.append(s1[i])
        encryptedS.append(s2[-(i+1)])

    #  if s1 is longer, append remaining characters
    if len1 > min_len:
        encryptedS.extend(s1[min_len:])

    #  if s2 is longer, append remaining characters
    if len2 >  min_len:
        encryptedS.extend(s2[:len2-min_len][::-1])

    # Join the list into a single string and return
    return ''.join(encryptedS)

s1 = input()
s2 = input()

print(shuffling(s1, s2)) 

# method 2
def shuffle_strings(str1, str2):
    # Reverse the second string for easier access to the last character
    str2_reversed = str2[::-1]
    
    # Determine the length of the longer string
    max_length = max(len(str1), len(str2))
    
    result = []
    
    # Interleave characters from both strings
    for i in range(max_length):
        if i < len(str1):
            result.append(str1[i])
        if i < len(str2_reversed):
            result.append(str2_reversed[i])
    
    # Join the result list to form the final string
    return ''.join(result)

# Input from the user
str1 = input("Enter the first string: ").strip()
str2 = input("Enter the second string: ").strip()

# Get the shuffled string
shuffled_string = shuffle_strings(str1, str2)

# Output the result
print(shuffled_string)


#Q5
'''
Income Tax PAN Validation
Tax Information Network (TIN) is an initiative by Income Tax Department of India (ITD) for the modernization of the current system for collection, processing, monitoring and accounting of direct taxes using information technology. The network will check the eligible entities based on Permanent Account Numbers (PAN).PAN contains ten-digits in which first five characters are letters, next four numerals, last character is a letter and all characters in PAN number is always uppercase.If the PAN given by the user follow the above format then it is a Valid PAN Number other wise Invalid PAN Number.
write a program to validate the PAN number.
 
Input and Output Format:
Input is string of any length of any case.
Output is string ,should print “Valid PAN Number” without quotes if input fits the PAN rules otherwise “Invalid PAN Number” without quotes.
Refer sample input and output for formatting specifications.
Sample Input 1:
ABCDE1234F
Sample Output 1:
Valid PAN Number

Sample Input 2:
12345ABCD3
Sample Output 2:
Invalid PAN Number'''

import re

def validate_pan(pan):
    # Define the regex pattern for a valid PAN number
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
    
    # Check if the input string matches the pattern
    if re.match(pattern, pan):
        return "Valid PAN Number"
    else:
        return "Invalid PAN Number"

# Input from the user
pan = input("Enter the PAN number: ").strip()

# Validate the PAN and print the result
print(validate_pan(pan))

