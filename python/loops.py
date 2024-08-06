fruits = ["apple","rambutan","orange","durian", "mango", "banana","grapes","papaya"]

# to print all the fuits in the list
for fruit in fruits:
    print(fruit)

#print the fruit which is in the even position
for fruit in fruits[::2]:
    print(fruit)


#print the fruit that has 6 characters
print("6 characters fruit")
for fruit in fruits:
    if (len(fruit) == 6):
        print(fruit)

multiplicants = [1,2,3,4,5,6,7,8,9,10]
multiplier = 5
for multiplicant in multiplicants:
    print (multiplicant, 'x',  multiplier, "=", multiplicant * multiplier)

numbers = range(1,13)

multiplicants = range(1,13)
multiplier = 5
for multiplicant in multiplicants:
    print (multiplicant, 'x',  multiplier, "=", multiplicant * multiplier)


products = ["cooking oil","ginger",'garlic', 'tomato','milk']
#go to the super market
multiplier = 5
#for product in products:
#    shelfno = search(product)
#   wakto(selfno)
#    pick(product)
#    addtocart(product)
#checkout(mycart)
#total = 0
#for prodct in mycart:
#   price = getprice(product)
#   total = total + price
#   addtobasket(product)
#dopayment(total)


#Take a number as input print all the digits in the number
mynumber = int(input("Enter the number: "))
#mynumber =12345
# do you have a list = no 
# how many digits do we have = don't know
# you have to use while loop

print("-----------------")
while (mynumber > 0):
    print(mynumber % 10)
    mynumber = mynumber //10

usernumber = int(input("Enter the number: "))
mynumber = usernumber
print("-------------------")
numberofdigits = len(str(mynumber))-1
while(mynumber > 0):
    print(mynumber // 10 ** numberofdigits)
    mynumber = mynumber % 10 ** numberofdigits
    numberofdigits = numberofdigits - 1

mynumber = str(usernumber)
print("---------------")
for number in mynumber:
    print(number)

#Hanafi Effect
num = str(usernumber)
i = 0
while i < len(num):
    print(int(num[i]))
    i += 1


fruits = ["apple","rambutan","orange","durian", "mango", "banana","grapes","papaya"]

# Only in python the for loop can have else part
# The code in the else part will get executed only when all the fruits are iterated fully
# The iteration is exhausted(there is nothing else lah to read)
for fruit in fruits:
    print(fruit)
    #if fruit == "durian" : break
else:
    print("All fruits are printed")

#Generate first 10 prime number
count = 10
givennumber = 2
while count > 0:
    for divisor in range(2,mynumber):
        if mynumber% divisor == 0: break        
    #if fruit == "durian" : break

    else:
        print(mynumber,"is prime number")


#continue keyword
multiplicants = [1,2,3,4,5,6,7,8,9,10]
multiplier = 5
for multiplicant in multiplicants:
    if multiplicant % 5 == 0: continue
    print (multiplicant, 'x',  multiplier, "=", multiplicant * multiplier)
