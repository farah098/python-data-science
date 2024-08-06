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


def UpdateMenu(fileDetail,fileAddress):
    choice = -1
    while choice != 0:
        print()
        print("---------------------")
        print("|    UPDATE MENU     |")
        print("---------------------")
        print("|0 - Back            |")
        print("|1 - Update Details  |")
        print("|2 - Update Address  |")
        print("---------------------")
        choice = keyboardInput(int, "Choice  [0,1,2]: ", "Choice must be Integer\n")
        if choice == 0:
            print("Thank you for using our system\n")
            # doMenu(filename)
        elif choice == 1:
            updateDetail(fileDetail)
        elif choice == 2:
            updateAddress(fileAddress)

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
        id_number = keyboardInput(str, "Please key in ID Number: ", "ID Number must be Integer\n")
        print()

        if(id_number not in id_numbers):
            print("Sorry ID Number not found\n")
        else:
            index = id_numbers.index(id_number)
            id_number, birthDate, age, gender, nationality, emergencyNum, blood, medicalCond = data[index]
            print(f"Birth Date (yy-mm-dd):{birthDate}\nAge:{age}\nGender:{gender}\nNationality:{nationality}\
                  \nEmergency Contact Number: {emergencyNum}\nBlood Type:{blood}\nMedical Condition:{medicalCond}\n")
            confirm = keyboardInput(str, "Are you sure you want to edit this person(y/n): ", "Confirmation must be String\n")
            print()

            if confirm == "y":
                # print("Let us edit")
                newbirthDate = keyboardInput(str, f"Birth Date (yy-mm-dd) ({birthDate}):","Birth date must be string", birthDate)
                newage = keyboardInput(int, f"Age ({age}): ", "Age must be Integer", age)
                newgender = keyboardInput(str, f"Gender ({gender}): ","Gender must be string",gender)
                newnationality = keyboardInput(str, f"Nationality ({nationality}): ","Nationality must be string",nationality)
                newemergencyNum = keyboardInput(str, f"Emergency Contact Number ({emergencyNum}): ","Emergency contact number must be string",emergencyNum)
                newblood = keyboardInput(str, f"Blood Type ({blood}): ","Blood type must be string",blood)
                newmedicalCond = keyboardInput(str, f"Medical Condition ({medicalCond}): ","Medical condition must be string",medicalCond)
                print()
                data[index] = [id_number,newbirthDate,newage,newgender,newnationality,newemergencyNum,newblood,newmedicalCond]
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
        id_number = keyboardInput(str, "Please key in IC Number: ", "IC Number must be Integer\n")
        print()

        if(id_number not in id_numbers):
            print("Sorry IC Number not found\n")
        else:
            index = id_numbers.index(id_number)
            id_number, unitNum, street, postcode, state, city, country = data[index]
            print(f"Unit Number:{unitNum}\nStreet:{street}\nPostcode:{postcode}\nState:{state}\
                  \nCity: {city}\nCountry:{country}\n")
            confirm = keyboardInput(str, "Are you sure you want to edit this person(y/n): ", "Confirmation must be String\n")
            print()

            if confirm == "y":
                # print("Let us edit")
                newunitNum = keyboardInput(str, f"Unit Number ({unitNum}):","Unit number must be string", unitNum)
                newstreet = keyboardInput(int, f"Street ({street}): ", "Street must be Integer", street)
                newpostcode = keyboardInput(str, f"Postcode ({postcode}): ","Postcode must be string",postcode)
                newstate = keyboardInput(str, f"State ({state}): ","State must be string",state)
                newcity = keyboardInput(str, f"City ({city}): ","City must be string",city)
                newcountry = keyboardInput(str, f"Country ({country}): ","Country must be string",country)
                data[index] = [id_number,newunitNum,newstreet,newpostcode,newstate,newcity,newcountry]
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

filename1= "fileDetail.txt"
filename2= "fileAddress.txt"
UpdateMenu(filename1,filename2)