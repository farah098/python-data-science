# any / all
# They are built in functions
# They take boolean list as parameter
# [True,True,False,True,False,False]
# If any function take the above list as parameter it will return True
# Any True becomes True (any == or)
# If all function take the above list as parameter it will return False
# All requires everything to be True (any == and)
# Check whether the given number is Prime Number
givenNumber = 11
divisors = range(2,givenNumber)
# a list is given and we are going to create another list
if (len([mynumber for mynumber in divisors if (givenNumber % mynumber == 0)]) == 0):
    print("Prime Number")
else:
    print("Not Prime Number")

if any([givenNumber % mynumber == 0 for mynumber in divisors]):
    print("Not Prime Number")
else:
    print("Prime Number")

# Prime Number
# Check whether the given number is Prime or not
# Check whether the input is prime or not
# Generate first 10 Prime numbers
# Generate prime numbers between 10 to 100
