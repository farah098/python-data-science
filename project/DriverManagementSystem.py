from os.path import exists
import datetime
import pandas as pd
from tabulate import tabulate

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

def noBlankInput(prompt):
    while True:
        value = input(prompt)
        if value != "":
            return value
        else:
            print("This field cannot be blank.")

def Registration(regfile):
    try:
        id_number = noBlankInput("Enter ID number [4 digits]: ")
        id_exists = False
        try:
            with open(regfile, "r") as file:
                next(file)  # skip the header
                for line in file:
                    details = line.split('|')
                    if details[0] == id_number:
                        id_exists = True
                        break
        except FileNotFoundError:
            pass
        if id_exists:
            print(f"ID number {id_number} already exists. Please try again.")
            return
        name = noBlankInput("Enter name: ")
        phone_number = noBlankInput("Enter phone number [10 digits]: ")
        email = noBlankInput("Enter email: ")
        while True:
            license_expiry_date_str = input("Enter license expiry date (YYYY-MM-DD): ")
            try:
                license_expiry_date = datetime.datetime.strptime(license_expiry_date_str, "%Y-%m-%d").date()
                break
            except ValueError:
                print("License Expiry must be in (YYYY-MM-DD) format")      
        
        with open(regfile, "at") as filehandler:
            filehandler.write(f"\n{id_number}|{name}|{phone_number}|{email}|{license_expiry_date}")
            print("Registration successful")
        
        try:
            with open("fileDetail.txt", "at") as file1:
                file1.write(f"\n{id_number}|birthdate|gender|medical condition")
        except Exception as e:
            print(f"An error occurred while writing to {file1}: {e}")
        
        try:
            with open("fileAddress.txt", "at") as file2:
                file2.write(f"\n{id_number}|postcode|city|state")
        except Exception as e:
            print(f"An error occurred while writing to {file2}: {e}")

    except Exception as e:
        print("An error occured with the registration", e)

def UpdateMenu(fileDetail,fileAddress):
    choice = -1
    while choice != 0:
        print()
        print("+-----------------------------+")
        print("|        UPDATE MENU          |")
        print("+-----------------------------+")
        print("|    0 - Back to Main Menu    |")
        print("|    1 - Update Details       |")
        print("|    2 - Update Address       |")
        print("+-----------------------------+")
        choice = keyboardInput(int, "Choice  [0,1,2]: ", "Choice must be Integer\n")
        if choice == 0:
            break
        elif choice == 1:
            updateDetail(fileDetail)
        elif choice == 2:
            updateAddress(fileAddress)
        else:
            print("Invalid choice. Enter a valid option.")

def updateDetail(filename):
    try:
        lines = None
        with open(filename,"rt") as filehandler:
            lines = filehandler.readlines()

        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        
        id_numbers = [record[0] for record in data]
        # print(id_numbers)
        id_number = keyboardInput(str, "Please key in ID Number [4 digits]: ", "ID Number must be Integer\n")
        print()

        if(id_number not in id_numbers):
            print("Sorry ID Number not found\n")
        else:
            index = id_numbers.index(id_number)
            id_number, birthDate, gender, medicalCond = data[index]
            print(f"Birth Date (YYYY-MM-DD):{birthDate}\nGender [M/F]:{gender}\nMedical Condition:{medicalCond}\n")
            confirm = keyboardInput(str, "Are you sure you want to edit this person(y/n): ", "Confirmation must be y/n\n")
            print()

            if confirm == "y":
                # print("Let us edit")
                newbirthDate = keyboardInput(str, f"Birth Date (YYYY-MM-DD) ({birthDate}):","Birth date must be string", birthDate)
                newgender = keyboardInput(str, f"Gender [M/F] ({gender}): ","Gender must be string",gender)
                newmedicalCond = keyboardInput(str, f"Medical Condition ({medicalCond}): ","Medical condition must be string",medicalCond)
                print()
                data[index] = [id_number,newbirthDate,newgender,newmedicalCond]
                # print(data)
                newlines = []

                for record in data:
                    line = "|".join(map(str, record)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()

                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)
                
                print("The data successfully updated!\n")

    except Exception as e:
        print("Something went wrong when we create the file:", e, "\n")

def updateAddress(filename):
    try:
        lines = None
        with open(filename,"rt") as filehandler:
            lines = filehandler.readlines()

        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        
        id_numbers = [record[0] for record in data]
        # print(id_numbers)
        id_number = keyboardInput(str, "Please key in ID Number [4 digits]: ", "ID Number must be Integer\n")
        print()

        if(id_number not in id_numbers):
            print("Sorry ID Number not found\n")
        else:
            index = id_numbers.index(id_number)
            id_number, postcode, city, state = data[index]
            print(f"Postcode:{postcode}\nCity:{city}\nState: {state}\n")
            confirm = keyboardInput(str, "Are you sure you want to edit this person(y/n): ", "Confirmation must be y/n\n")
            print()

            if confirm == "y":
                # print("Let us edit")
                newpostcode = keyboardInput(str, f"Postcode ({postcode}): ","Postcode must be string",postcode)
                newcity = keyboardInput(str, f"City ({city}): ","City must be string",city)
                newstate = keyboardInput(str, f"State ({state}): ","State must be string",state)
                data[index] = [id_number,newpostcode,newcity,newstate]
                # print(data)
                
                newlines = []

                for record in data:
                    line = "|".join(map(str, record)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()

                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)
                
                print("The data is successfully updated\n")

    except Exception as e:
        print("Something went wrong when we create the file:", e,"\n")

def ReportMenu():
    choice = -1
    while choice != 0:
        print()
        print("+------------------------------------+")
        print("|            REPORT MENU             |")
        print("+------------------------------------+")
        print("|    0 - Back to Main Menu           |")
        print("|    1 - Overview                    |")
        print("|    2 - Driver Details              |")
        print("|    3 - Driver Additional Details   |")
        print("|    4 - Driver Address              |")
        print("+------------------------------------+")
        choice = keyboardInput(int, "Enter Choice [0, 1, 2, 3, 4]: ", "Enter a valid choice\n")
        
        driversdf = pd.read_csv("Driver.txt", sep="|")
        detailsdf = pd.read_csv("fileDetail.txt", sep="|")
        addressdf = pd.read_csv("fileAddress.txt", sep="|")
        driverdetail = pd.merge(driversdf, detailsdf, on="ID Number", how="left")
        driveraddress = pd.merge(driversdf, addressdf, on="ID Number", how="left")
        driverall = pd.merge(driverdetail, addressdf, on="ID Number", how="left")

        dataframes = [driverall, driversdf, driverdetail, driveraddress]
        for df in dataframes:
            df['ID Number'] = df['ID Number'].fillna('0').apply(lambda x: str(x).zfill(4))
            df['Phone Number'] = df['Phone Number'].fillna('0').apply(lambda x: str(x).zfill(10))

        pd.set_option('display.max_columns', None)
        #pd.set_option('display.max_colwidth', 20)
        pd.set_option('display.width', 1000)
        pd.set_option('display.show_dimensions', True)
        pd.set_option('display.colheader_justify', 'center')
        pd.set_option('display.notebook_repr_html', False) 

        if choice == 0:
            break
        elif choice == 1:
            driverall.index = driverall.index + 1
            print(tabulate(driverall.fillna('None'), headers='keys', tablefmt='pretty', showindex=True))
        elif choice == 2:
            driversdf.index = driversdf.index + 1
            print(tabulate(driversdf, headers='keys', tablefmt='pretty', showindex=True))
        elif choice == 3:
            driverdetail.index = driverdetail.index + 1
            print(tabulate(driverdetail.fillna('None'), headers='keys', tablefmt='pretty', showindex=True))
        elif choice == 4:
            driveraddress.index = driveraddress.index + 1
            print(tabulate(driveraddress, headers='keys', tablefmt='pretty', showindex=True))
        else:
            print("Invalid choice. Enter a valid option.")

def CheckLicenseExpiry():
    today = datetime.date.today()
    threemonths = today + datetime.timedelta(days=90)

    try:
        with open("Driver.txt", "r") as file:
            next(file) # skip the header
            for line in file:
                details = line.strip().split("|")
                idnumber = details[0]
                name = details[1]
                expirydate = datetime.datetime.strptime(details[4], "%Y-%m-%d").date()
                if today <= expirydate <= threemonths:
                    print(f"Alert: {name} (ID: {idnumber}) needs to renew their license soon! License Expiry Date: {expirydate}")
    
    except Exception as e:
        print("An error occured:", e)
            
def display_menu():
    print()
    print("+-------------------------------------------------------------+")
    print("|            Welcome to Driver Management System              |")
    print("+-------------------------------------------------------------+")
    print("|                     1 - Registration                        |")
    print("|                2 - Update Driver Information                |")
    print("|                         3 - Report                          |")
    print("|              4 - Alert for Driving License Expiry           |")
    print("|                         0 - Exit                            |")
    print("+-------------------------------------------------------------+")
    choice = input("Enter your choice: ")
    return choice

regfile = "Driver.txt"
filename1= "fileDetail.txt"
filename2= "fileAddress.txt"

while True:
    choice = display_menu()
    if choice == "0":
        break
    elif choice == "1":
        Registration(regfile)
    elif choice == "2":
        UpdateMenu(filename1,filename2)
    elif choice == "3":
        ReportMenu()
    elif choice == "4":
        CheckLicenseExpiry()
    else:
        print("Invalid choice. Enter a valid option.")
