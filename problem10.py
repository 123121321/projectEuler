# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# importing numpy as reading and writing for math ops is faster
import numpy as np

# function that implements a seive of eratosthenes algorithm

def range_check(n,m):
    if n < m//2:
        return(True)

def prime_Sieve(n):
    print("populating sieve")
    # populate a list from 2 to n before making it an np array
    temp_Sieve = []
    i = 2
    while i <= n:
        temp_Sieve.append(i)
        i += 1
    sieve = np.array(temp_Sieve)
    primes = np.array([])
    del temp_Sieve
    print("Sieve looks like this")
    print(sieve)
    i = 0
    in_Range = True
    while in_Range == True:
        if range_check(sieve[i],n) == True:
            np.append(primes,sieve[i])
            j = 1
            N = sieve[i]*j
            if range_check(N,n) == True:
                sieve = sieve[sieve != N]
                j += 1
            else:
        else:
            np.concatenate((primes, sieve))
            
                
    print("Primes up to n are" + primes)

prime_Sieve(20)

