# Methods are nothing but function inside the class
# Methods take at least 1 parameter (self)
# This parameter is used by python to pass the instance 

class calculator:

    def __init__(self,x,y):
        self.x= x
        self.y= y

    def add(self):
        return self.x + self.y
    
    def sub(self):
        return self.x - self.y

# the value kept in an instance variable
mycalculator = calculator(10,20)
print(mycalculator.add())
print(mycalculator.sub())


# Class method
class Utility:

    def add(x,y):
        return x + y
    
    def sub(x,y):
        return x - y

print(Utility.add(10,20))

# however this can be easily done just using module in python
# no need to create a class

#  There are some use cases where class has properties


# class Customer:
    
#     def __init__(self) -> None:
#         pass

