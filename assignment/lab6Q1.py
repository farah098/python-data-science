'''
def multiplication_table(num):
    for i in range(1,13):
        multi = num * i
        print(f"{num} x {i} = {multi}")
        
num = int(input("Enter Number: "))
print(f"\nMultiplication table of {num}")
multiplication_table(num)

# method 2
def multiplication_table(num):
    results = []
    for i in range(1, 12):
        multi = num * i
        results.append(f"{num} x {i} = {multi}")
    return "\n".join(results)

num = int(input("Enter Number: "))
print(f"Multiplication of {num}")
print(multiplication_table(num))
'''

def change(one, *two):
    print(type(two))
change(1,2,3,4)