firstname = "Khairi"
lastname = "Abu Bakar"
# + arithmatic operator used for addition 
# to perform addition both side of + must be integer or float

# however if both sides are string then python performs
# string concatenation
fullname = firstname + " " + lastname
print(fullname)

carplate = "JCG"
number = 9876

# I can only concatenate str (not "int") to str
# JCG cannot be converted to number 
# 9878 can be converted to string 
# we use the built in  function str to convert
# in this case one is string (JCG) another one is number (9876)
# python does not know whether to perform addition or
# string concatenation
carplatenumber = carplate + str(number) 
print(carplatenumber)

# we also know * means multiplication
# how can we use * over string data
product = "book"
# when u multiplying string with integer then the * becomes time operator
print(product *5)
print("=" * 50)

'''
# variable is something varying
# equation,expression is a model
product = "Television" #literal/value
#literal is a value 
'''

# We already know strings value (string literal) in python are enclosed 
# either with double quote "" or single quote ''

# How we handle such this traditionally
# slash \ is also called escape sequence
# When this \ is followed by some letter it has meaning
# \n = new line character 
# \t = tab character
# \r = carriage character
content= 'As I am not \t feeling well\n'
content= content + 'I am not able to \ attend class\n'
content= content + 'please proceed the class without \rme \n'
print(content)



filepath = "C:\newfolder\table\readme.txt"
print(filepath)
# escape sequence
filepath = "C:\\newfolder\\table\\readme.txt"
print(filepath)
# raw string
filepath = r"C:\newfolder\table\readme.txt"
print(filepath)

# However in python you can use """...""" or '''...'''
# to handle multiline strings
content= '''
As I am not feeling well 
I am not able to attend class
please proceed the class without me
'''
print(content)

# '''...''' is a valid python statement 
# they(python) don't know what to do 
# because we do not assign it to any variable
'''
As I am not feeling well 
I am not able to attend class
please proceed the class without me
'''

# Relationship between strings and list
# strings are nothing but list of characters
message = "Hello world" # ['H','e','l','l','o','','w','o','r','l','d']
print(message[0])
print(message[0:5])
print(message[-5:])
print(message[::-1])

mynumber = 86749
# strmynumber = str(mynumber)
# print(int(strmynumber)[::-1])
print(int(str(mynumber)[::-1]))

numbers = input("Enter the numbers (comma seperated): ")
print(numbers)
print(type(numbers))
numbers.split(",")
values = numbers.split(",")
print(values)
print(type(values))

total = 0
for value in values:
    total = total + int(value)
print(total)


