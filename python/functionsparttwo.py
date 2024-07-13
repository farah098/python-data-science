# Whenever we say function immediately we think about
# 2 things 1) parameter 2) return
# We already know how to pass function as an argument
# we are going to see how to return function
def authenticate(username, password): # parent
    def simpleInterest(principle,period, rate): # child
        def something(): # Grand child
             pass
        something()
        return(principle * period * rate)/ 100
    if (username == "admin" and password == "pwd123"):
        # now we know function can have inner function
        # inner function can be called from the outer function
        # how ever you vannot call the innerfunction
        # from the main context 
        #print("Interest amount: ",simpleInterest(1000, 1, 6))
        return simpleInterest()

func = authenticate ("admin","pwd123")
print("Interest amount",func(1000,1,6))
# why  inner function
# sometimes the authenticate function itself will get bloated
# and you may come across there are few statements you copy and 
# pasted it multiple times inside the function
# its good to convert those statements to inner function

def sum(a,b):
    return a + b

# function without name is also called anonymous function
# however if the function do not have a name how to call/invoke them
# based on our diagram can we write function as
# sum = def(a,b):
#    return a + b

x = 10
def sayX():
    print(x)
sayX()

# however python still has lambda function
# lambda function can have only one statement
# lambda function are written in one line 
def add(x,y):
    return x + y
# Step 1: convert your function to an anonymous function
# def(x,y): return x + y
# Step 2 : we cannot call the no name function (annonymous function)
# let us assign the function to a variable 
# # sum = def (x,y): return x+ y
# Step 3 : rename def with lambda 
# sum = lambda ( x.y): return x + y
# Step 4: parenthesis "()" and "return" keyword can be remove
sum =lambda x,y : x+y 
print(add(10,20))
print(sum(10,20))


farenheitvalues = [32,33,34,35,36,37,38,39,40]
celciusvalues = []
for farenheitvalue in farenheitvalues:
    celciusvalues.append((farenheitvalue - 32)* 5/9)
print("Celcius values using for loop:", celciusvalues)
# Or 
celciusvalues = [(farenheitvalue - 32)* 5/9 for farenheitvalue in farenheitvalues]
print("Celcius values using for list comprehension:", celciusvalues)

celciusvalues = map(lambda value: (value - 32)* 5/9, farenheitvalues)
print("Celcius values using map:", list(celciusvalues))

