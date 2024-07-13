# list 
fruits = ["apple", "orange", "mango", "banana"]
for fruit in fruits:
    print(fruit)


# overseafruits = fruits # we should not do this 
# overseafruits = fruits.copy()

# we iterate through the list and create a new list
# the number of items in the newly created list is same as the original list
overseafruits = []
for fruit in fruits:
    overseafruits.append(fruit)
print("Copy using for loop:", overseafruits)

overseafruits = [fruit for fruit in fruits]

prices = [ 10,20,30,40,50]
priceswithsst = []
for price in prices:
    priceswithsst.append(price + (price * 0.06 ))
print("Prices with sst using for loop:", priceswithsst)
#Or
priceswithsst = [price + (price  * 0.06) for price in prices] # other way to write 
print("Price with sst using for list comprehension: ", priceswithsst)

# using a class called map
# it will return map object (iterator)
# Step 1: convert the expression into a function
def calculateSST(price):
    return price + (price *0.06)
priceswithsst = map(calculateSST,price)

# You can write either way
farenheitvalues = [32,33,34,35,36,37,38,39,40]
celciusvalues = []
for farenheitvalue in farenheitvalues:
    celciusvalues.append((farenheitvalue - 32)* 5/9)
print("Celcius values using for loop:", celciusvalues)
# Or 
celciusvalues = [(farenheitvalue - 32)* 5/9 for farenheitvalue in farenheitvalues]
print("Celcius values using for list comprehension:", celciusvalues)



# iterate and create a new list 
# then you can use something called "List comprehension"
# List + For Loop => List comprehension
# instead of creating the traditional for loop we can do it using List comprehension

# we iterate through the list of values and create a new list
# the number of items in the newly created list is less than or same as
# the original list

multipleofthree = []
for number in range(0,16):
    if (number % 3 == 0): multipleofthree.append(number) # append it conditionally
print("Multiples of three using for loop: ", multipleofthree)

multipleofthree = [number for number in range(0,16) if (number % 3 == 0)]
print("Multiple of three using for list comprehension:", multipleofthree)

def isMultipleOfThree(number):
    return True if (number % 3 == 0) else False

# using a class called map 
# it will return map object (iterator)

numbers = [9,4,2,3,7,6,5,4,3,22,44,55,66]
evennumbers = []
for number in numbers:
    if (number % 2 == 0): evennumbers.append(number)
print("Even Number using for loop:", evennumbers)
#Or 
evennumbers = [number for number in numbers if (number % 2 == 0)]
print("Even Number using for list comprehension:", evennumbers)

def isEven(number):
    return True if (number % 2 == 0) else False
evennumbers = filter(isEven, numbers)
print("Even numbers using filter", list(evennumbers))

# we iterate through the list of values and we reduce it to a single value
# the number of items in the newly created list is less than or same as
# the original list
numbers = [1,2,3,4,5]
total = 0
for number in numbers:
    total = total + number
print("Total using for loop: ", total)

# Since we reduce the list to a single value we cannot use list comprehension
# However we can use another function called reduce (not built in)
# which is inside a module called functools (builtin module)
from functools import reduce

numbers = [1,2,3]

def calculateTotal(previous, current):
    return previous + current

print("Sum using reduce: ", reduce(calculateTotal, numbers))

'''
def reduce(func, values):
    sum = 0
    for value in values:
        sum = func(sum, value)
    return sum'''

def calculateFactorial (previous, current):
    return previous * current

print("Factorial using reduce: ", reduce(calculateFactorial, numbers))

# now the sum will be initialized with 5
print("Factorial using reduce: ", reduce(calculateFactorial, numbers, 5))
