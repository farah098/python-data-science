# product is the variable
# Television is the string value/literal
# to differentiate the variables from values we use double quote ""
# or single quote ''
# product  = 'Television'

product ="Television"
quantity = 2 #integer
price = 1455.25 #float
available = True #True/False (boolean value/literal)

print("Product:", product)
print("Quantity:", quantity)
print("Price:", price)
print("Available:", available)

#type is another built in function that tells us what is the
#data type of the variables (dynamiclly assigned by python)print("Product:", product)
print(type(product))
print(type(quantity))
print(type(price))
print(type(available))

total = quantity * price
print("Total:", total)

# In real world use cases the 10 will not be hard coded 
# the 10 is coming from an input device (keyboard)
# So the input value can be a string which needs to be converted
quantity = "10"
print(type(quantity))
price = "1455.55"
# print(quantity * price)

# type casting 
# convert one data type to another 
# to convert string to integer we have a built in function int 
# to convert string to float we have a built  in function float
total = int(quantity) * float(price)
print(total) 

total1 = float(price) // int(quantity)
print(total1)

firstNumber = 500
# how can i see the address where the object 500 is 
#In python we have a built in function called "id"
print(id(firstNumber))
secondNumber =500
print(id(secondNumber))

firstString = "Hello"
secondString = "Hello"
print(id(firstString))
print(id(secondString))

# so far we have seen how to assign one value to one value in variable in one line
# however we can also assign more that one value to more than one variable in 1 line
x, y = 101, 102 # we assign values to variables (initialization)
print(x)
print(y)

# however  in  python the following is not supported 
# x, y = 105
x, y = 101 + 1, 102 + 2
print(x)
print(y)


# Initialization
x = 0 # numeric initializer 
x = "" #string initilixer / empty string 
x = None # no brain
print(type(None))