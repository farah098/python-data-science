# Has-A relationship
# Customer has-a passport

class Passport:

    def __init__ (self,country,passportnumber):
        self.country = country
        self.passportnumber = passportnumber

    def __str__(self):
        return f"Country: {self.country} \nPassport Number: {self.passportnumber}"


class Customer:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = ""
        self.passport = None
    
    def __str__(self):
        message = f"First Name: {self.firstname}\n" 
        message = message + f"Last Name: {self.lastname}\n" 
        message = message + f"IC Number: {self.icnumber}\n"
        if (self.passport != None):
            message = message + self.passport.__str__()
        return message

peter = Customer("Parker","Peter")
passport = Passport("UK", "E0283892")
peter.passport = passport # assign object to peter
print(peter)
# now we know how to convert a python object to dictionary
print(peter.__dict__)
