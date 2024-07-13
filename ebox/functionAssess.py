# Q1 Multiple 2 numbers using default arguments
def multiply(a, b):
    c = a * b     
    return f"The result is {c}"

a = int(input())
b = int(input())

print(multiply(a,b=10))
print(multiply(a,b))
print(multiply(a,b=9))


# Q2 Displaying user inputs using multiple return values
def multiVarFunc():
    department = input("Enter department name:")
    student = int(input("Enter the number of total students:"))
    faculties = int(input("Enter the number of total faculties:"))

    return department, student, faculties
    # return f"Department:{department}", f"Total students:{student}", f"Total faculties:{faculties}" 

department, student, faculties = multiVarFunc()
print("Details:")
print(f"Department:{department}")
print(f"Total students:{student}")
print(f"Total faculties:{faculties}")

#2 METHOD
# print(department)
# print(student)
# print(faculties)
