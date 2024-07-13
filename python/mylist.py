# List is a data structure / sequence
# list is denoted using square bracket []
# List allow duplicates
# List is modifiable 
# List is ordered
# List is indexed
# Data inside the list is heterogenous
# the data can be of different types

# Let us create a list 
fruits = ["apple", "orange", "mango", "banana", "grapes"]
# fruits is a variable which can hold more than one value
# fruits is also an object, instance of list (class)
# Jegan, John are objects, instance of Human (class)
# Jegan has 2 eyes, 1 noese (properties) (what he has)
# Jegan can walk,eat, run teach, listen (methods) (what he can do)
quantity = [10,20,30,40,50]
# quantity is a variable which can hold more than one value
# quantity is also an object, instance of list (class)

# Indexing and Selection
# plese refer to variablestwo.py

# Can add more items to the existing list
fruits.append("durian")
print(fruits)


# you can insert items into the existing list
# insert is another method we have in the list class
fruits.insert(1, "rambutan")
print(fruits)
fruits.insert(3, "Cempedak")
print(fruits)

# how to modify an existing item 
fruits[5] = "mangosteen"
print(fruits)

# how can i remove grapes
# remove is another method we have in the list class
fruits.remove("grapes")
# however thid will remove only first instance of grapes
# if have 2 grapes (1 have and 1 remove)
# can use loop to remove
print(fruits)

# how can i remove an item using index
# there is no method to do this 
# however we can use del keyword
# del keyword will delete anything from memory permanently
#del everything
myname = "Jegan"
del myname
#print(myname)

del fruits[3]
print(fruits)

#clear all the items in the list
fruits.clear()
print(fruits)
del fruits
#print (fruits)

fruits = ["apple", "orange", "mango", "banana", "orange","grapes"]
if ("orange" in fruits):
    print(fruits.index("orange")) # only give the first index
    print(fruits[fruits.index("orange")+1:].index("orange") + fruits.index("orange") + fruits.index("orange"))
    # fruits.index("orange") => 1
    # fruits.index("orange") => 2
    # fruits[2:] => ["mango", "banana", "orange","grapes"]
    # fruits[2:].index("orange") => 2........(2)
    # 2 + 1 + 1



# you can also use built in function called enumerate
# enumerate is a function used to find index of every item in the list
enumeratedfruits = enumerate(fruits)
print(enumeratedfruits)
# enumerate object is also an iterable object
# in the for loop => for fruit in fruits
# fruits is a list 
# fruits must be iterable object
# however print function do not know how to iterate it so it prints the
fruitlist = (enumeratedfruits)
print(fruitlist)
# the enumerated list is a list of tuples 
# each tuple has 2 value
# 1) index
# 2) fruit (item)
for item in fruitlist:
    if (item[1] == 'orange'): print(item[0])

# shallow copy
x = [10,20,30,40,50,60,70]
y = x
print(x)
print(y)
x[2]=35
print(x)
print(y)

# deep copy
x = [10,20,30,40,50,60,70]
# y  = x Don't do this
# y = []
y = x.copy()
for i in x:
    y.append(i)
print('=' * 40)
print(x)
print(y)
x[2]=35
print(x)
print(y)

fruits = ["apple", "orange", "mango"]
# x is a variable
# 10 is a literal 
# when we assign 10 to x,x is an object 
# since we assign 10(integer), x becomes an object/instance of int class

# this parenthesis () is really confusing
# to call/invoke anything in python we use the operator () round bracket
# to call/invoke a function print(), id(), range()
# to create an object also list()

# fruits = ["apple", "orange", "mango"]
# fruits is a variable
# ["apple", "orange", "mango"] is a literal (collection)
# when we assign ["apple", "orange", "mango"] to fruits, fruits beccomes an object
# since we assign ["apple", "orange", "mango"] (list), fruits becomes and object/instance of list

# product = "Television"
# product is a variable
# "Television" is a literal 
# when we assign "Television" to product, product becomes an object 
# since we assign "Television" (string), product becomes an object/instance of string class


fruits = list(["apple","orange","mango"])
print(fruits)


# there is one feature which list and tuple has 
# auto explode
fruits = ("apple", "orange", "mango")
fruit01 = fruits[0]
fruit02 = fruits[1]
fruit03 = fruits[2]
print(fruit01,fruit02,fruit03)
# the above is manual explode
# However you need to do this in python list
fruit01, fruit02, fruit03 = fruits
print(fruit01,fruit02,fruit03)

#In tuple we have one problem
x = (10) # we are trying to assign a tuple with 1 item 10
# python will interpret this as expression that returns single value
print(x)
print(type(x))



