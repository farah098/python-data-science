# Multiple inheritance
class Card:
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside Card Class")

class AtmCard(Card):
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside Atmcard Class")

class CreditCard(Card):
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside CreditCard Class")

class DebitCard(Card):
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside DeditCard Class")

class BankCard(AtmCard,CreditCard,DebitCard):
    def __init__(self):
        pass
    def doSomething(self):
        #print("Inside BankCard Class")
        super().doSomething()

# we have created 5 classes
# and in all 5 classes we have dosomething method 
# and it is implemented (got code inside which is print)

# Let us create instance of the last card
bankCard = BankCard()
bankCard.doSomething()

# now remove the print statement from bankcard.something
# and call the super().something()
# this time u will see "Inside AtmCard Class" (which is the first inherited class)

# now comment the dosomething method which is inside the AtmCard Class
# this time you will see "Inside CreditCard Class"

# now comment the dosomething method which is inside the CreditCard Class
# this time you will see "Inside DeditCard Class"

# now comment the dosomething method which is inside the DebitCard Class
# this time you will see "Inside Card Class"

# Basically what we understand here is 
# python scan from left to right and identify the base classes
# and call the method accordingly
# This process is called Method Resolution Order (MRO)
print(BankCard.__mro__)

# <class '__main__.BankCard'>
# <class '__main__.AtmCard'>
# <class '__main__.CreditCard'>
# <class '__main__.DebitCard'>
# <class '__main__.Card'>
# < class 'object'>

# BIGGEST CONCLUSION:
# Every class we create in python is inherited from a class called object 
#class DebitCard(Card):
# def __init__():
#     pass
# def __str__():
#     print(memory address)

class Student():
    #pass 
    def __str__(self):
      return "Student"

class Alumni():
    pass 
    #def __str__(self):
    #  return "Alumni"

alumni = Alumni()
print(alumni)
# it is override so output will be Alumni
# every class inherited from class from object 

# Iterator object like enumerator, range, map, filter do not override
# the method __str__
# However those classes are inherited from the default python class
# called object which has the method __str__ which
# returns the address location of the object
# Finally that gets printed using the print function

#############################
# Print address location only
# Object is parent by default
class Object:
    pass
    #def __str__(self):
    #  return "Address"

class Alumni(object):
    pass 
    #def __str__(self):
    #  return "Alumni"

alumni = Alumni()
print(alumni)
class range(object):
    pass

myrange = range()
print(myrange)
# What if i dont want my class to inherit from the base class called object
# Definetly you don't want to do this because
# you will loose all the default feature of a class

class myclass:
    pass


# myclass().will list more methods
# now we understand those methods are coming the base class called object

# No I insist I dont want my class to be inherited
class noObjectClass():
    pass

test = noObjectClass()
print(test)


