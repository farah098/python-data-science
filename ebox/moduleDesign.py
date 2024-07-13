#Q1
'''
Module: Fibonacci Series
The teacher was teaching about number series generation and one of the series is like she will write first two number of the series and each student has to write a next number of the series on the board and next number will be the addition of previous two numbers and first two numbers will be 0 and 1. 
So, help the students by writing a program to generate the Fibonacci series.

Input Format:  
The input consists of integer which represents 'n' as number of values in the series

Output Format:
The output consists of series of integer numbers.

Sample Input 1:
3
Sample Output1:
0 1 1

Sample Input 2:
6
Sample Output2:
0 1 1 2 3 5

'''
import math

def fibonacci(n):
    series = [0,1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return ' '.join(map(str,series[:n]))

n = int(input())
print(fibonacci(n))


#Q2
'''Module: Factorial Number
A Mother wants to teach his 4th standard son about the factorial of a number. She told that the product of an integer and all the integers below, it is called a factorial of that number. Then she gave him a number to find the factorial of that number. So help that kid to find the factorial of that number.
Thus, write a program to find the factorial of a given number.
Input Format:  
The input consists of an integer which represents a number.
Output Format:
The output consists of an integer value represents factorial of that number.
Note: All text in bold corresponds to input and the rest corresponds to output.
Sample Input and Output:
3
6'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input()) 
print(factorial(n))


#Q3
'''Element Search

In a school, class teacher wants to organize a game for L.K.G students and 
the game is like there will be a  basket  with numbered balls teacher will 
give one number and student has to search for that particular  numbered ball 
if student found that  numbered ball  then he has to say "Got It!" otherwise  "Sorry!".
Help the students to write a program to search the numbered ball.

Input  Format: 

The first line of input corresponds to the number of balls in the basket,n.
The next n  line of input consists of the numbered balls in the basket.
The last line of input consists of a numbered ball to be searched.

Output Format:

The output is a  string consist of 'Got It!' or 'Sorry!' (without quotes).
[All text in bold corresponds to input and the rest corresponds to output.]

Sample Input and Output 1:

5
21
18
90
6
74
6
Got It!

Sample Input and Output 2:

5
21
18
90
6
74
10
Sorry!'''

n = int(input())
basket = [] 

for i in range(n):
    basket.append(int(input()))

search_ball = int(input())
found = False

for ball in basket:
    if ball == search_ball:
        found = True
        break

if found:
    print("Got It!")
else:
    print("Sorry!")


#Q4
'''Module: Word Count
Teacher organize a debate competition, In order to check the student's talking skills, 
she will write a list of topics in cards, student has to pick one of the cards then she 
wants to group the student based on the topics they have selected  and she will name the group 
based on the topic's name.
Now help her to find a number of students in each group.

Input Format:
The first line of input is a string consists of lower case letter words  (each word will indicate topics selected by the student)


Output Format:
The output consists of a count of each word.

Note: All text in bold corresponds to the input and the rest corresponds to output.

Sample Input and Output:
mother father mother GST father GST facebook facebook GST
facebook-2
father-2
gst-3
mother-2
'''
import collections

n = input()
count = collections.Counter(n.split())
print(f"Enter the String")
for key, count in sorted(count.items()):
    print(f"{key}-{count}")

#Q5
'''
Module: GCD of Two Numbers

The greatest common divisor (GCD) of two or more integers, which are not all zero, is the largest positive integer that divides each of the integers. After the explanation given by tuition teacher, now he wants to conduct the small test to check their understanding of GCD concept.
So, help the students by writing a program to find the GCD of Two Numbers.

Input  Format: 
The input consists of two integers.

Output  Format:
The output consists GCD of Two Numbers.

Note: All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output:
Enter the two positive numbers
12
14
GCD:2
'''

def gcd(a,b):
    while b:
        a, b = b , a % b
        return a

print("Enter the two positive numbers")
n1 = int(input())
n2 = int(input())

result = gcd(n1,n2)

print(f"GCD:{result}") 


# Q6
'''Module: First Non-Repeating Character
Sandhya and Pooja are playing string game. And Sandhya gives a string to Pooja, and she has to find a first non-repeating character from that string. So help Pooja by writing a program to find the first non-repeating character from that string.
Input Format:
The input consists of a string.
Output Format:  
The output consists of a character which represents the first non-repeating character.
If there is no non-repeating character in the string, then print '#'.
Note: All text in bold corresponds to input and the rest corresponds to output.
Sample Input and Output 1:
swiiss
w

Sample Input and output 2:
naddan
#
'''

word = input().lower()

char_count = {}

for i in word:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1

for i in word:
    if char_count[i] == 1:
        print(i)
        break
else:
    print("#")

#Q7
'''Write a program to calculate maximum and minimum number from the given user input.
Note : Use built-in function only.
Input and Output Format :
(Refer sample input and output)
[All text in bold corresponds to input and rest others are output]
Sample Input and Output :
Enter the values:
1 4 6 12 73 92 134
The maximum value is : 134
The minimum value is : 1'''

n =   input("Enter the values:\n").split(" ")
list_n = []
for num in n:
    list_n.append(int(num))
# print(list_n)

max_n = max(list_n)
min_n = min(list_n)

print(f"The maximum value is : {max_n}")
print(f"The minimum value is : {min_n}")

#Q8
'''
Write a program to find the character based on the ASCII value given by the user as an input. Display the character based on the ascii value provided by the user.
Note : Refer to the problem requirements
Input and Output Format :
(Refer to sample input and Output)
[All text in bold corresponds to input and rest others are output]
Sample Input and Output :
Enter the value :
65
Character of ASCII value 65 is  A 
'''

ascii = int(input("Enter the value :\n"))

char = chr(ascii)

print(f"Character of ASCII value {ascii} is{char}")




