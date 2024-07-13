'''
n = int(input())
s = 0 
while n != 0:
    d = n % 10
    s += d
    n //= 10
print("Sum", s)

n = 6
i = 0 
while i < n:
    print(i)
    i += 1
print("outside loop")

n = 6
for i in range(n):
    if i == 4:
        break
    print(i)     
else:
    print("inside else, reached end of for loop")


#PRIME NUMBER
n = int(input())
for i in range(2,n):
    if n % i == 0:
        print("Composite")
        break
else:
    print('prime')

'''
