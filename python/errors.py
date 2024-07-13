x = 10
 
# Syntaxx Error
# if (x % 2 == 0):
# print("Even Number") # >> indentation error
 
# Logical error
# if (x % 2 == 0):
#     print(f"Given Number is {x}")
# print("Even Number")

# Runtime Error

try:
    # we know the following line is taking user input
    # in future this may throw error
    # then you must place this code inside a block called
    # try except
    # another example put the file open code here
    principle = int(input("Principle: "))
except ValueError: 
    # when that error occur what we must do
    # the code inside the except block will get executed
    # only when an error occurs
    # another example throw the errors file corrupted / 
    print("Principle amount must be an Integer")
    # principle = 1000
except Exception as e:
    print("Something went wrong:", e)
else:
    # The code inside the else block gets executed 
    # only when there is no error
    print("All is well")
finally:
    # The code inside this finally block will always gets executed
    # regardless of whether an error occur or not
    print("Thank you")


# The program does not get terminated abnormally


period = int(input("Period: "))
rate = int(input("Rate: "))
interest = (principle * period * rate) / 100
