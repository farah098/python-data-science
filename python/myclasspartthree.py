# Encapsulation
# Encapsulate the properties inside the class
# in other languages we have keywords public, private, protected
# to protect the properties 

class circle:
    
    def __init__(self,radius):
        # change the property with single underscore 
        # this make the property private
        self.__radius = 0
        if (isinstance(radius, int)):
            self.__radius = radius
        else:
            print("Invalid Radius")

    # getter and setter method
    def getRadius(self): 
        return self.__radius 
    
    def setRadius(self,radius): # set value to the property
        if(isinstance(radius,int)):
            self.__radius = radius
        else:
            print("Invalid radius")
    
    # property is a class
    # We are calling/invoking the class by passing the method as argument
    # Please notice after getRadius there is no ()
    # the property class returns the property object which is assigned to 
    # a variable radius 
    # in other words radius is an instance of property class
    radius = property(getRadius,setRadius) # new property


    def area(self):
        return 3.14 * self.__radius * self.__radius
    
    def circumference(self):
        return 2 * 3.14 * self.__radius
    
    def __str__ (self):
        return f"Radius of this circle is {self.__radius}"


mycircle = circle(20)
print(mycircle)

#mycircle = circle("abc")
print(mycircle)

#mycircle.__radius = 30

# you are indirectly passing the value to the setter method
mycircle.radius = 30
print(mycircle)

# you are indirectly passing the value to the setter method
# mycircle.__radius = "abc"
# print(mycircle)

print(mycircle.area())
# print(mycircle.getRadius())
# print(mycircle.setRadius(2))
print(mycircle)

# do not use object. single or double underscore to access property outside the class