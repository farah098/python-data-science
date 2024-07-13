# object - instance of a class
# Class - blue print
'''
class
    characteristics/data member/state
    functionalities/member function/behavior
'''

class Person: # self represent current object
    def __init__(self, age, g, h, w): #constructor
        self.age = age
        self.gender = g
        self.height = h
        self.weight = w
    
    def display(self):
        print("Person Details: ")
        print("Age =",self.age)
        print("Gender =",self.gender)
        print("Height =",self.height)
        print("Weight =",self.weight)
    
    def __str__(self):
        return str(self.age) + "," +self.gender + "," +\
        str(self.height) + "," + str(self.weight)

p1 = Person(25,'M',178,82)
p2 = Person(22,'F',166,45)

print(p1.age) #25
print(p2.gender) #F

p1.display() 
# Age = 25
# Gender = M
# Height = 178
# Weight = 82

print(p1) 
# if there is def __str__ it print the __str__ function
# if there is NO it will print address location of class
print(p2)
# if there is def __str__ it print the __str__ function
# if there is NO it will print address location of class

#-------------------------------------------------------------------------------------------------------
'''
access specifiers

public -  no underscores - can be accessed anywhere
protected - one underscore - should be accessed by the inherited classes
private - 2 underscore - should not be accessed anywhere except in the same class
'''
# how to access private variable?
class Person: # self represent current object
    def __init__(self, age, gender, height ): #constructor
        self.age = age
        self._gender = gender
        self.__height = height

p = Person(25,"M",175)

print(p.age)
print(p._gender)
# print(p.__height)

#-----------------------------------------------------------------------------------------------------

''' Getter setter'''

# def getAge - camel case
# def get_age - snake case

class Person: # self represent current object
    def __init__(self, age): #constructor
        self.age = age

    def getAge(self):
        return self.age
    
    def setAge(self,age):
        self.age = age

    def __str__(self):
        return "age = " + str(self.age)
    
p = Person(45)
print(p.getAge())
p.setAge(27)
print(p)

#---------------------------------------------------------------
class Person: # self represent current object
    def __init__(self, age): #constructor
        self.age = age

    def getAge(self):
        return self.age
    
    def setAge(self,age):
        self.age = age

    def delAge(self,age):
       self.age = age

    def __str__(self):
        return "age = " + str(self.age) 
    
    
p = Person(45)
p.age = 27