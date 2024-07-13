class Gender:
    def __init__(self):
        pass
    def doCarryObjects(self):
        pass

class Male(Gender):
    def __init__(self):
        pass
    def doCarryObjects(self):
        print("Carry Heavy Objects")

class Female(Gender):
    def __init__(self):
        pass
    def doCarryObjects(self):
        print("Carry Light Objects")

def getGender(name):
    if "A/L" in name:
        return Male()
    else:
        return Female()

# Python dynamically set the data type for the gender variable
# it could be Male or Female Object 
gender = getGender("Khairi A/L Abu Bakar")
gender.doCarryObjects()

gender = getGender("Aida A/P Abu Bakar")
gender.doCarryObjects()
print(type(gender))

getGender