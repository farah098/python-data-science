
"""
This one use for string that want to 
write string and comments in multiple
line
"""
#multiline = """ 
#Hello world.
#This is Farah
#I need to tell you something
#Bye"""
#print ("multiline: " + multiline)

"""
#1st video
age = 24
age = str(age)
print("My age is " + age)

single_quote_inside_praised = "You're are so beautiful"
print(single_quote_inside_praised)

response = 'I said "Thank you " '
print(response)

#Not recommended to do 
other_response = "He said \"You are amazing!\" yesteday." # escaping
print(other_response)

#string 
age = 24
print(f"My age is {age}")

name ="Jose"
final_greeting = "How are you, {name}?"
jose_greeting = final_greeting.format(name ="Jose")
print(jose_greeting)

#other method
name ="Jose"
final_greeting = "How are you, {}?"
print(final_greeting.format(name ))

print(" ")
friend_name ="Jose"
final_greeting = "How are you, {name}?"
print(final_greeting.format(name = friend_name))

#Input statement
#split n number of input enter by the user
a = input("Enter number: ")
al = a.split() #a list
print(al)
x, y, z = map(int,al)
print(x,y,z)
print(type(a))

x,y,z = map(int,input("Enter number: ").split(" "))
print(x,y,z)




#float 
#format specifier
#int - %d
#float =%f
#str - %s

a = 12.353535
b = 22
c = "is my weight"

print("%f"%a)
print("%.2f"%a)
print("%d - %.3f : %s" %(b,a,c))
print("%d %s" %(b,c))

age = 34
print(type(age))



#loops

r = 4
c = 6

for i in range(r): # 0 1 2 3 --> rows
    for j in range(c): # 0 1 2 3 5--> colums
        print(i,end=" ")
    print()



n = int(input())

for i in range(n):
    for j in range(n):
        if ( i == j or i + j == n - 1):
            print("*", end=" ")
        else:
            print("$", end=" ")
    print()


for i in range(6):
    for j in range(i+1):
        print("o",end=" ")
    print()

# Get the number of Armstrong numbers to generate from the user
num_armstrong_numbers = int(input("Enter the number of Armstrong numbers to generate: "))

# List to store Armstrong numbers
armstrong_numbers = []

# Initialize the number to be checked
num = 0

# Loop to find the required number of Armstrong numbers
while len(armstrong_numbers) < num_armstrong_numbers:
    # Convert the number to a string to iterate over digits
    digits = str(num)
    num_digits = len(digits)
    
    # Calculate the sum of digits each raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    
    # Check if the sum of powers is equal to the number
    if sum_of_powers == num:
        armstrong_numbers.append(num)
    
    # Move to the next number
    num += 1

# Print the Armstrong numbers
print(f"The first {num_armstrong_numbers} Armstrong numbers are:")
for armstrong_number in armstrong_numbers:
    print(armstrong_number)

num = 1
for i in range(1,10):
  num += 1 
  
  if (num % i != 0):
    prime = i
  print(f"{prime} prime")

  

#Question 8
import sys

# display all elements 
print("\nAll elements: ", end=" ")
for i in sys.argv:
  print(i,end=" ")
print("\n")

# diplay all elements in even position
print("Even Position")
print('-' * 10)
print("Position", "Elements")
for i in range(1,len(sys.argv)):
  if (i % 2 == 0):
    print("  ",i, "     ", sys.argv[i])
print()

#diplay all elements in odd position
print("Odd Position")
print('-' * 14)
print("Position", "Elements")
for i in range(1,len(sys.argv)):
  if (i % 2 != 0):
    print("  ",i, "     ", sys.argv[i])
print()





#Question 9
import sys

total = 0

for i in sys.argv[1:]:
    total = total + int(i)
avg = total / len(sys.argv)
print(f"Average: {avg:.2f}\n")


  
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()



prime = []

num = 2

while(len(prime) < 10):

    divisor= []

    for i in range(2,num):
        if (num != i):
            if (num % i == 0):
                divisor.append(i)

    if (len(divisor) == 0):
        prime.append(num)
    
    num += 1

for i in prime:
    print(i,end=" ")
    


    

# Get the number of Armstrong numbers to generate from the user
num_armstrong_numbers = int(input("Enter the number of Armstrong numbers to generate: "))

# Pre-allocate a list to store Armstrong numbers
armstrong_numbers = [0] * num_armstrong_numbers

# Initialize the number to be checked
num = 0
count = 0 

# Loop to find the required number of Armstrong numbers
while count < num_armstrong_numbers:
    # Convert the number to a string to iterate over digits
    digits = str(num)
    num_digits = len(digits)
    
    # Calculate the sum of digits each raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    
    # Check if the sum of powers is equal to the number
    if sum_of_powers == num:
        armstrong_numbers[count] = num
        count += 1
    
    # Move to the next number
    num += 1

# Print the Armstrong numbers
print(f"The first {num_armstrong_numbers} Armstrong numbers are:")
for armstrong_number in armstrong_numbers:
    print(armstrong_number,end=" ")




n = int(input("Enter number: "))

while n > 0:
  r = n % 2
  n = n // 2

  result = str(r) 

result = str(r) + result

print(result)
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(0)

n = int(input())
s = 0 

while n != 0:
    d = n % 10 # to get the numbers from every digit number
    s += d # sum of the digits
    n //= 10
print(f"sum {s}")
N = int(input())

odd_list = []
odd =30
series1 = 0

for i in range(N//2 + 1) : # odd placement 
    odd  +=  series1
    series1 += 8
    odd_list.append(odd)

#print(odd_list)

even_list = []
even = 35
series2 = 0

for i in range(N//2) : # even placement 
    even  +=  series2
    series2 += 6
    even_list.append(even)

#print(even_list)

combined_list = [None] * N

even_index_count = 0
odd_index_count = 0

for i in range(N):
    if i % 2 == 0: # 0, 2, 4
        combined_list[i] = odd_list[even_index_count]
        even_index_count += 1
    else: # 1 , 3
        combined_list[i] = even_list[odd_index_count]
        odd_index_count += 1

#print(combined_list)

for i in combined_list:
    print(i, end=' ')


A, B, N = input().split(" ")

A = int(A)
B = int(B)
N = int(N)

C,D = 0,0
scores = 0 
for i in range(N):
    if (i % 2 == 0):
        A = A * 2
    else:
        B = B * 2
scores = A + B
print(scores)

N  = int(input())

registration = []

for i  in range(N): # loop for user input
    n = int(input())
    registration.append(n)
print(registration)

import sys

total = 0

for i in sys.argv[1:]:
    total = total + int(i) # total value in the
avg = total / len(sys.argv)# average need to be out of the loop cuz it is divisible by the total of the index
print(f"Average: {avg:.2f}\n")


#iAsses
a = int(input())
b = int(input())
count = 0

while a <= b:
    isPrime = True
    for divisor in range(2, a):
        if (a  %  divisor == 0):
            isPrime = False 
            break 

    if isPrime == True:
        count += 1
        print(a)
    a += 1
   


#iAsses Loop
a = int(input())
b = int(input())
for i in range(a,b+1):
    if (i > 1):
        for divisor in range(2, i):
            if (i %  divisor == 0):break 
        else:
            print(i,end=" ")
   """

def greet(argument1,argument2 = "Welcome to Python Programming"):
    return f"Hello {argument1}, {argument2}"

print("Menu")
print("1. Name and Message" )
print("1. Name" )
n = int(input())
if  n == 1:
    argument1 = input("Enter the name ")
    argument2 = input("Enter the message ")

elif n == 2:
    argument1 = input("Enter the message ")

print(greet(argument1,argument2))