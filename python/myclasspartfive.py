# Is- A relationship
# Alumni is a student
class Student:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = ""
    
# Alumni extends Student class
class Alumni(Student):# passs student as an argument
    #pass # it take parent __init__ method

    #calling __init__ method statically
    def __init__(self, firstname, lastname,alumninumber):# calling the init function of the parent
    #     Student().__init__(self,firstname, lastname)
    #     pass
    
    # Or
    # can use the keyword super class
    # which will return the object of parent child 
        super().__init__(firstname,lastname) # parent punya attribute
        self.alumninumber = alumninumber

    
    def __str__(self):
        return f"First Name: {self.firstname}\
            \nLast Name: {self.lastname} \
            \nIC Number: {self.icnumber}\
            \nAlumni Number: {self.alumninumber}"
    

# we have created an object of alumni class
alumni = Alumni("Peter","Parker", 898932)
print(alumni)