# 3 July 2024
# you should not hardcode the data inside the program as follows
# you must keep apple, orange, mango in a txt file or csv file or excel file
# you must write a python program to read the data
# from the file and do the necessary things (print/process)
# in other words data must be separated from the program
 
# You must create a file using python code
# you can use the keyword open
# open('fruits.txt')
# the open built in function takes 2 parameters
# 1) filename and 2) mode
# we have to give instruction to python if the file does not exist create it
####################################################################################
# we call such extra instruction as mode
# Mode
# 1. x create the file if it does not exists
# 2. t this is going to be a text file
# 3. b this going to be a binary file
# 4. w this will let us to write inside the file. However this will clear
#    the existing content inside the file.
# 5.
############################################################
# open('fruits.txt', 'xt')

# When we run it again we get an error and its File already exists
# we suppose to check whether the file already exists
# import os
# os.path.exists('filename')
# from os import path
# path.exists('filename')
from os.path import exists

def keyboardInput(datatype, caption, errorMessage, defaultValue = None):
    value = None 
    isInvalid = True 
    while(isInvalid):
        try:
            if defaultValue == None:
                value = datatype(input(caption))
            else:
                value = input(caption)
                if value.strip() == "":
                    value = defaultValue
                else:
                    value = datatype(value)
        except:
            print(errorMessage)
        else:
            isInvalid = False
    return value

# if exists(filename):
#     pass
# else:
#     open(filename, 'xt')
def createFile(filename):
# the open buit i function oppen the file and return the handler
# which can use to read / write inside the file 
    if not exists(filename):
        try:
           filehandler = open(filename, 'xt')
        except Exception as e:
            print("Something went wrong when we create the file", e)
        else:
            createTitle(filename)
        finally:
            # filehandler has many methods like read, write and close
            filehandler.close()
# filename = "fruits.txt"
# createFile(filename)

# content = input("Fruit Name: ")
# filehandler = open(filename, '')

# open built in function
# no close built in function

# with is a keyword
# whenever came out of the block, the resource will be closed automatically
def createTitle(filename):
    try:
        with open(filename,'wt') as filehandler: 
            # "Television|20|1455.55"
            filehandler.write("Product|Quantity|Price")
    except Exception as e:  
        print("Something went wrong when we create the file:", e)

def addProduct(filename):
    try:
        product = keyboardInput(str, "Product:","Product must be String")
        quantity = keyboardInput(int, "Quantity: ", "Quantity must be Integer")
        price = keyboardInput(float, "Price: ","Price must be float")
        with open(filename,"at") as filehandler:
            filehandler.write(f"\n{product}|{quantity}|{price}")
    except Exception as e:  
        print("Something went wrong when we create the file:", e)

def printProduct(filename):
    try:
        lines = None
        with open(filename,"rt") as filehandler:
            lines = filehandler.readlines()
        # for line in lines:
        #     product, quantity, price = line.strip().split("|") # strip() method in str class that remove \n character
        #     print(f"{product:40}{quantity:>20}{price:>20}")
        for index, line in enumerate(lines):
            product, quantity, price=line.strip().split("|")
            if (index == 0):
                print(f"{"No":5}{product:40}{quantity:>20}{price:>20}")
                print("=" * 80)
            else:
                print(f"{index:<5}{product:40}{int(quantity):>20}{float(price):>20.2f}")


    except Exception as e:
        print("Something went wrong when we create the file:", e)

def doMenu(filename):
    choice = -1
    while choice != 0:
        print("------------")
        print("|0 - Exist  |")
        print("|1 - List   |")
        print("|2 - Add    |")
        print("|3 - Edit   |")
        print("|4 - Delete |")
        print("------------")
        choice = keyboardInput(int, "Choice  [0,1,2,3,4]: ", "Choice must be Integer\n")
        if choice == 0:
            print("Thank you for using our system")
        elif choice == 1:
            printProduct(filename)
        elif choice == 2:
            addProduct(filename)
        elif choice == 3:
            editProduct(filename)
        elif choice == 4:
            delProduct(filename)

def editProduct(filename):
    try:
        lines = None # because dont know what data type
        with open(filename,"rt") as filehandler: # assign filehandler as variable 
            lines = filehandler.readlines()

        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        index = keyboardInput(int, "Please key in index of the Product: ", "Index must be Integer\n")
        
        if(index >= len(data)):
            print("Sorry product not available")
            print(len(data))
        else:
            product, quantity, price = data[index]
            print(f"Product:{product}\nQuantity:{quantity}\nPrice:{price}")
            confirm = keyboardInput(str, "Are you sure you want to edit this product (y/n): ", "Confirmation must be String\n")
            
            if confirm == "y":
                # print("Let us edit")
                newproduct = keyboardInput(str, f"Product ({product}):","Product must be String", product)
                newquantity = keyboardInput(int, f"Quantity ({quantity}): ", "Quantity must be Integer", quantity)
                newprice = keyboardInput(float, f"Price ({price}): ","Price must be float",price)
                data[index] = [newproduct,newquantity,newprice]
                # print(data)
                newlines = []

                for product in data:
                    line = "|".join(map(str, product)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)

    except Exception as e:
        print("Something went wrong when we create the file:", e)


def delProduct(filename):
    try:
        lines = None
        with open(filename,"rt") as filehandler:
            lines = filehandler.readlines()

        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        index = keyboardInput(int, "Please key in index of the Product: ", "Index must be Integer\n")
        
        if(index >= len(data)):
            print("Sorry product not available")
            print(len(data))
        else:
            product, quantity, price = data[index]
            print(f"Product:{product}\nQuantity:{quantity}\nPrice:{price}")
            confirm = keyboardInput(str, "Are you sure you want to delete this product (y/n): ", "Confirmation must be String\n")
            
            if confirm == "y":
                # print(data)
                del data[index]
                newlines = []

                for product in data:
                    line = "|".join(map(str, product)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)
                    
    except Exception as e:
        print("Something went wrong when we create the file:", e)



filename = "fruits.txt"
createFile(filename)
# addProduct(filename)
# printProduct(filename)
doMenu(filename)

