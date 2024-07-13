# Python dictionary is also called JSON in other languages
# JSON = JavaScript Object Notation
# Dictionary is represented using {}
# Dictionary is ordered (retain its position)
# Dictionary is index using key(s) (not using numbers 0,1,2,3...)
# Dictionary does not allow duplicate keys but allow duplicate value)
# Every data is associated with a key
# Here firstname is a key and Peter is a value
foreigner = {
    "firstname" : "Peter",
    "lastname" : "Parker",
    "passportnumber" : "E485476",
    "incometaxnumber" : "SG382832",
    "lastmonth" : 5,
    "lastyear" : 2024,
    "lastamount" : 854,
    "transactions" : [(4,2024,852),(3, 2024, 850),(2, 2024, 853),(1,2024,854)],
    "address" : { # key
        "office" : { # dictionary inside dictionary
            "street": "15 Lorong 67/9",
            "taman" : "Equine park"
        },
        "home" : { #cannot duplicate key inside dictionary
            "street": "223 Jalan SS9",
            "taman" : " Subang Jaya"
        }
    }
}
print(f"First Name: {foreigner["firstname"]}")
print(f"Last Name: {foreigner["lastname"]}")
print(f"Passport Number: {foreigner["passportnumber"]}")
print(f"Income Tax Number: {foreigner["incometaxnumber"]}")
print(f"Last Paid Month: {foreigner["lastmonth"]}")
print(f"Last Paid Year: {foreigner["lastyear"]}")
print(f"Last Amount Paid: {foreigner["lastamount"]}")

for month, year, amount in foreigner["transactions"]:
    print(f"{month}-{year}  RM{amount}")

officeaddress = foreigner["address"]["office"]
print(officeaddress["street"])
print(officeaddress["taman"])

officeaddress = foreigner["address"]["home"]
print(officeaddress["street"])
print(officeaddress["taman"])

officestreet = foreigner["address"]["home"]["street"]
print(officestreet)

# Dictionary is modifiable
# how to add a new key
# since the key car does not exists inside the foreigner dictionary
# it gets added automatically
foreigner ['car'] = { # new key added
    "brand" : "Proton", # entire dictionary added
    "model" : "SAGA",
    "carplatenumber" : "JDU3843"
}

print(foreigner)
foreigner['contact'] = " 0112672632"
print(foreigner)

# how can i modify an existing data inside the dictionary
#  since the key are already exists inside the dictionary it will update the data 
foreigner['contact'] = "0198382932"
print(foreigner)

# how to drop a key
foreigner.pop('car')
print(foreigner)

for key in foreigner.keys():
    if (isinstance(foreigner[key], list)):
        for item in foreigner[key]:
            print(item)
    elif (isinstance(foreigner[key], dict)):
        for innerkey in foreigner[key].keys():
            print(foreigner[key][innerkey])
    else:
        print(key, foreigner[key])

for key,item in foreigner.items():
    print(key, item)

# empty the dictionary
foreigner.clear()
print(foreigner)