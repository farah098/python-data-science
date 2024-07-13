def TwinPrimeNumber():
    prime = []

    # get the prime number 
    for num in range(2,1000):
        isPrime = True
        for i in range(2,num):
            if num % i == 0:
                isPrime = False
                break
        if isPrime == True:
            prime.append(num)
        num += 1
    
    #return prime

    twin_prime = []
    #while i < (len(prime) +1): #3,5,7,11
    for i in range(1,len(prime)):
        if (prime[i] - prime[i-1]) == 2: # need to i-1 not i+1 because i+1 gonna be out of range (but i-1 gonna be 0)
            twin_prime.append((prime[i-1], prime[i]))
    return twin_prime
            

print("Twin Prime Number ")
for i in TwinPrimeNumber():
    print(f"{i[0]} and {i[1]}")








