from math import *

prastevilo = []

def is_prime(number):
    # 1 is a special case of not prime
    if number <= 1:
        return False
    # 2 is a special case of a prime
    if number == 2:
        return True
    # check if the number divides by 2 with no remainder
    if number % 2 == 0:
        return False
    # limit on divisors we test, sqrt of n, +1 so range() will reach it
    limit = floor(sqrt(number)) + 1
    # check for evenly divisible for odd numbers between 3 and sqrt(n)
    for i in range(3, limit, 2):
        # check if number is divisible with no remainder
        if number % i == 0:
            # number is divisible and is not a prime
            return False
    # number is probably prime
    prastevilo.append(number)
    return True



for x in range(2, 101):
    is_prime(x)
print(prastevilo)
