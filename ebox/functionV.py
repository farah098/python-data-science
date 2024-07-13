# stack model
# last in first out
 
def sumOfTwoNumbers(a,b):
    print("Inside sum function")
    c = a + b
    return c # if no return (default value return is None)

print("Inside main")
a = 5
b = 1
c = sumOfTwoNumbers(a,b)
print("sum: ",c)



#recursion - a function calling (a copy) itself
# code looks simple 
'''
def fun(args):
    if(base/exit condition):
        stmts
        return

    return recursive call/calls
factorial 
5! = 5*4*3*2*1
4! = 4*3*2*1
3! = 3*2*1
2! = 2*1
1! = 1
0! = 1

 n! = n*(n-1)!

 fibonacci
 0 1 1 2 3 5 8 13 21

 f(n)= f(n-1) + f(n-2)



def fact(n):
    if n == 1 or n == 0:
        return 1
    return n*fact(n-1)

n = int(input())
f = fact(5)
print(f)

'''

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)


def sum(a=5,b=10,d= 20, e=30):
    print("a = ", a)
    print("a = ", b)
    print("a = ", d)
    print("a = ", e)

    c = a + b + d + e
    return c

print(sum(50))
print(sum(50, b = 90))
print(sum(50,e = 50))
print(sum(50,60,90,100))
