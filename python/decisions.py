# Find whether the given number is positive, negative or zero
# find whether my business is making profits, loss or break even (takde untung)

expenses = 1000
sales = 1100

#Objective 1: Please print only when we have profit
if (sales > expenses):
    # this is called block
    # "block" means one or more than one statement to be executed
    print ("You are making profit")

#Objective 2: Please print when we have profile and loss
if (sales > expenses):
    print("You are making profit")
else:
    print("You are making loss")

#Objectives 3: Please print when we have profit, loss and breakeven
if (sales > expenses):
    print("You are making profit")
else:
    if (sales == expenses):
        print("You are at Breakeven")
    else:
        print("You are making losses")


if (sales > expenses):
    print("You are making profit")
elif (sales == expenses):
    print("You are at Breakeven")
else:
    print("You are making losses")

print("The END")

# When you have single line of statement to be executed
# When the condition is true/false then we can use the following 
# if syntax.

# I want you to find whether the given number is even 
givenNumber = 6
if (givenNumber % 2 == 0) : print("Even Number")

#Find whether the given number is even or odd
givenNumber = 7
print("Even Number") if (givenNumber % 2 == 0) else print ("Odd Number")

# find whether the given number is positive, negative or zero
givenNumber = 5
print("positive") if (givenNumber >0) else print("negative") if (givenNumber <0) else print ("Zero")


# expression using shorthand if
x = 15
y = 10
op = "+"
# result = x + y if (op == "+") else result  = x - y
# In python the if condition behave like a function that returns a value
# result = function()
result = x + y if (op == "+") else x - y
