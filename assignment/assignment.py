"""
#Question 1
Integer = int(input("Please enter number : " ))
if (Integer % 2 == 0):
  print("It is an even number")
else:
  print("It is an odd number")

#Question 2
score = int(input("Please enter the score: "))
if (score >= 90 and score<=100):
    print("The score is A")
elif(score >= 80 and score <= 89):
    print("The score is B")
elif(score >= 70 and score <= 79):
    print("The score is C")
elif(score >= 60 and score <= 69):
    print("The score is D")
elif(score >= 0 and score < 60):
    print("The score is F")
else:
    print("No grade")

#Question 3


#Question 4
a = input ("Enter first number: ")
b = input ("Enter second number: ")
c = input ("Enter third number: ")

if (a > b and a > c):
    Num = a
elif (b > a and b > c):
    Num = b
else:
    Num = c

print (Num + " is the largest number")

# Question 5
characters = input("Enter a character: ")
if (characters == 'a' or characters == 'e' or characters == 'i' or characters == 'o' or characters == 'u'):
    print ("The character is vowel")
if (characters == 'A' or characters == 'E' or characters == 'I' or characters == 'O' or characters == 'U'):
    print ("The character is vowel")
else:
    print ("The character is consonant")


#Question 6
weight = float(input("Weight: "))
height = float(input("Height: "))

BMI = weight / (height ** 2)
print ("BMI: ", BMI)

if (BMI < 18.5):
    cate = "underweight "
elif (BMI >= 18.5 and BMI < 24.9):
    cate = "normal weight"
elif (BMI >= 25 and BMI < 29.9):
    cate = "overweight"
else:
    cate = "obesity"

print ("You are " + cate)




#Question 7
x = 6
y = 8
z = 10

if (x == y and y == z and z == x):
    print("Equilateral")
elif (x == y or y == z or z == x):
    print("Isosceles")
else:
    print("Scalene")


#Question 3
year = 1884
# year can be divided by 400 and it is kiraan for century year 
if (year % 400 == 0 and year % 100 == 0):
    print ("It is leap year ")
# year can be divided by 4 and it is kiraan for not century year 
elif (year % 4 == 0 and year % 100 !=0 ):
    print ("It is leap year")
else :
    print("It is normal year")


#Question 8
amount = int(input("Enter the amount you want to withdraw: "))
#amount = 233
amount50 = amount // 50 #4
remainder50 = amount % 50 #33
amount20 = remainder50 // 20 #1
remainder20 = remainder50 % 20 #13
amount10 = remainder20 // 10 #1
remainder10 = remainder20 % 10 #3

if(amount % 10 == 0):
    print("RM50: ", amount50)
    print("RM20", amount20)
    print("RM10", amount10)
else:
    print("Please put the right amount. This machine can withdraw RM50, RM20 and RM10 only")

#Question 9

num = int (input("Enter number (2 digit only) : "))
#condition for input number that ONLY accept 2 digit
if(num >= 0 and num <= 99):
    sq_num = 0
    sq_num = num ** 2 #square of the number
    print("Square input number: ", sq_num)

     #Reversion of input number
    rev_num = ((num % 10) * 10) + (num // 10)
    print("Reversion of input number: ", rev_num)

    
    # calculation for reversion square
    sq_rev_num = rev_num ** 2 # square of the reversion input number 
    print("Square of reversion of input number", sq_rev_num)
    rev_sq_rev_num = 0
    if (sq_rev_num >= 10 and sq_rev_num <= 99): #condition for the value that have 2 digit
        rev_sq_rev_num =(sq_rev_num % 10) + (sq_rev_num // 10)
    elif(sq_rev_num >= 100 and sq_rev_num <= 999): #condition for the value that have 3 digit
        rev_sq_rev_num =((sq_rev_num % 10) * 100)
        rev_sq_rev_num =((sq_rev_num // 10) % 10) * 10 + rev_sq_rev_num
        rev_sq_rev_num =(sq_rev_num // 100) + rev_sq_rev_num
    else: #condition for the value that have 4 digit
        rev_sq_rev_num =((sq_rev_num % 10) * 1000)
        rev_sq_rev_num =((sq_rev_num // 10) % 10) * 100 + rev_sq_rev_num
        rev_sq_rev_num =((sq_rev_num // 100) % 10) * 10 + rev_sq_rev_num
        rev_sq_rev_num =(sq_rev_num // 1000) + rev_sq_rev_num
    print("Reversion of Square of reversion of input number ",rev_sq_rev_num)


    #condition for adam number
    if(sq_num == rev_sq_rev_num ):
        print ("This is Adam number")
    else:
        print ("This is not Adam number")

else:
    print("Please enter 2 digit number ONLY")


#Question 10

num = int(input("Enter number: "))

#condition for input number calculation according to the number of digits
if (num >= 0 and num <= 9999):
    if (num >= 0 and num < 10):
        arm_num = num ** 1
    elif (num >=10 and num <= 99):
        num1 = (num // 10) ** 2
        num2 = (num % 10) ** 2    
        arm_num = num1 + num2
    elif (num >= 100 and num <= 999):
        num1 = (num // 100) ** 3
        num2 = ((num // 10) % 10) ** 3
        num3 = (num % 10) ** 3   
        arm_num = num1 + num2 + num3
    else:
        num1 = (num // 1000) ** 3
        num2 = ((num // 100) % 10) ** 3
        num3 = ((num // 10) % 10) ** 3
        num4 = (num % 10) ** 3   
        arm_num = num1 + num2 + num3 +num4
    
    if (num == arm_num):#condition for armstrong
        print("This is Armstrong number")
    else:
        print("This is not Armstrong number")

else:
    print("Please enter number that have up to 4 digits ONLY")

#Question 1
greeting = f"Welcome to Amphi Event Management System"

#Question 2
name = input("Enter your name\n")
greet = print(f"Hello {name:.50} ! Welcome to Amphi Event Management System")

#Question 3
brand = int(input("Enter the branding expenses "))
travel = int(input("Enter travel expenses "))
food = int(input("Enter food expenses "))
logistics = int(input("Enter logistics expenses "))

total = brand + travel + food + logistics

out_total =print(f"Total expenses : Rs.{total:.2f}")
out_brand =print(f"Branding expenses percentage : {brand //1000:.2f}%")
out_travel =print(f"Travel expenses percentage : Rs.{brand //1000:.2f}%")


#question 4
x = int(input(f" Enter the value of X\n"))
y = int(input(f"Enter the value of Y\n"))

c = (y -5 *x) /13
a = c + x 
s = 2 * c
print(f"Number of children tickets sold : {int(c)}")
print(f"Number of adult tickets sold : {int(a)}")
print(f"Number of senior tickets sold : {int(s)}")

mynumber = 1
while (mynumber <= 10): # condition natural numbers
    print(mynumber)
    mynumber = mynumber + 1
for i in range(1,20):
    if (i % 5 != 0):
        print(i)
num = 1

for i in range(num,31):
  print(i, end=' ')

strNumbers = input("Enter the numbers (comma seperated): ")

listStrNumbers = strNumbers.split(",")
listNumbers = []

for strNumber in listStrNumbers:
  listNumbers.append(int(strNumber))

#create list of unique numbers 
uniqueNumbers = []
for count in range(0, len(listNumbers)):
    if listNumbers[count] not in uniqueNumbers:
       uniqueNumbers.append(listNumbers[count])

index = 0
for outputvariable1 in uniqueNumbers:
    innerindex = index + 1
    for outputvariable2 in uniqueNumbers[innerindex:]:
        outputvariable3 = 100 - (outputvariable1 + outputvariable2)
        if(outputvariable3 in uniqueNumbers[index + 1:]):
            print(outputvariable1, outputvariable2, outputvariable3)
            break 
        innerindex = innerindex + 1
    index = index +1 
    


#Question 4
# Step 1: Get the Number of Armstrong Numbers to Generate from the User
num_items = int(input("How many Armstrong numbers do you want? "))

# Step 2: Find and Print Armstrong Numbers
count = 0
current_num = 0

while count < num_items:
    # Count the number of digits in the current number
    num_digits = len(str(current_num))

    # Initialize a variable to store the sum of digits raised to the power of num_digits
    sum_of_digits = 0
    temp_num = current_num

    # Loop through each digit in the current number
    while temp_num > 0:
        digit = temp_num % 10
        sum_of_digits += digit ** num_digits
        temp_num //= 10

    # Check if the current number is an Armstrong number
    if current_num == sum_of_digits:
        print(current_num)
        count += 1
    # Move to next number
    current_num += 1


print("Enter 2 integers")
A = int(input("A :"))
B = int(input("B :"))

if A > B:
    count = 0
    while count >= 0 :

        if (A == 0) or (B == 0):
            if (A == 0):
                print (B)
            elif (B == 0):
                print (A)
            break
        else: 
            R = A % B
            Q = A // B
            A = B
            B = R
        
        count += 1
else:
    print("Warning !!! Please enter integer A greater than integer B")

def compress_string(s):
    compressed = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    
    # Append the last set of characters
    compressed.append(s[-1] + str(count))
    
    # Join the list into a single string
    compressed_string = ''.join(compressed)
    
    # Return the original string if compression does not reduce size
    return compressed_string if len(compressed_string) < len(s) else s

def main():
    s = input("Enter a string to compress: ")
    compressed = compress_string(s)
    print(f"Compressed string: {compressed}")

if __name__ == "__main__":
    main()
    
"""  


'''
prime = []

num = 2

while(len(prime) < 10): # 0 - 9

    divisor= []

    for i in range(2,num): # 2
        if (num != i):  # 2 != 2
            if (num % i == 0): # 
                divisor.append(i)

    if (len(divisor) == 0): # satisfied the condition
        prime.append(num) #append into prime = []

    num += 1 # 3 = 2 + 1

for i in prime: # display 2 in prime variable
    q = (2 ** i) - 1 # use formula 
    if 
      perfect =  (2**(i-1)) * q
      print(perfect)

#Q6 lab 05
import timeit
start = timeit.default_timer()

count = 0
givenNumber = 2
no = 1
print("No", " ", "Perfect Number")
while (count < 10):
    isPrime = True
    for divisor in range(2,givenNumber):
        if (givenNumber % divisor == 0):
            isPrime = False 
            break
  
    
    if isPrime:
        #print(givenNumber, end= " ")
        p = givenNumber
        q = 2 ** p - 1

        for i in range(2,q):
            if(q % i == 0):
                isPrime = False 
                break
    
        if isPrime:
            perfect = (2 ** (p-1)) * q
            print(no, " ", perfect)
            count += 1
            no += 1
    givenNumber += 1


end = timeit.default_timer()
print("Run time: ", end - start)


#Q10
def compress_string(s):
    compressed = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    
    # Append the last set of characters
    compressed.append(s[-1] + str(count))
    
    # Join the list into a single string
    compressed_string = ''.join(compressed)
    
    # Return the original string if compression does not reduce size
    return compressed_string 


s = input("Enter a string to compress: ")
compressed = compress_string(s)
print(f"Compressed string: {compressed}")



# Q9
def roman_num(num):
    if num > 39999:
        print("Enter number less than 3999!")
        return
    value = [10000, 9000, 5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbol = ["X̅", "I̅X̅", "V̅", "I̅V̅", "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = ''
    i = 0
    while num > 0:
        div = num // value[i]
        num = num % value[i]
        while div:
            roman += symbol[i]
            div -= 1
        i = i + 1
    return roman


def int_num(roman):
    roman = roman.upper()
    value = [10000, 9000, 5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbol = ["X̅", "I̅X̅", "V̅", "I̅V̅", "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    num = 0
    i = 0
    while i < len(roman):
        if roman[i:i+2] in symbol:
            num += value[symbol.index(roman[i:i+2])]
            i += 2
        else:
            num += value[symbol.index(roman[i])]
        i += 1
    return num

num = int(input("Enter a number: "))
print(f"{num} in Roman is: {roman_num(num)}")
print("========================================")
num = input("Enter a Roman numeral: ")
print(f"{num} in integer is: {int_num(num)}")
'''



def combination(n, r):
    if r == n or r == 0: return 1
    if r == 1 : return n
    return combination(n-1, r) + combination(n-1, r-1)

n = int(input("Enter n: "))
r = 0

for i in range(n):
    for j in range(n-i+1):
        print(" ", end="")
    for j in range(i+1):
        print (combination(i,j), end=" ")
    print()