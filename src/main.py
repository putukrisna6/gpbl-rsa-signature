NUMBER_OF_EVALUATION = 4

from algorithms.millerRabin import isPrime
from algorithms.millerRabin import millerRabin

def getTwoPrimes(n):
    primeNumbers = []
    while(len(primeNumbers) < 2):
        if (isPrime(n, NUMBER_OF_EVALUATION)):
            primeNumbers.append(n)
        n += 1
    return primeNumbers

print(getTwoPrimes(10))
