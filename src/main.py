NUMBER_OF_EVALUATION = 4

from algorithms.millerRabin import isPrime
from algorithms.eulerTotient import phi
from helper.calculations import power
from helper.calculations import relativelyPrime
from helper.calculations import modInverse
from helper.strings import textToAscii
from helper.strings import asciiToText

def getTwoPrimes(n):
    primeNumbers = []
    while(len(primeNumbers) < 2):
        if (isPrime(n, NUMBER_OF_EVALUATION)):
            primeNumbers.append(n)
        n += 1
    return primeNumbers[0], primeNumbers[1]

def getE(phiN):
    e = -1
    for i in range(2, phiN):
        if (relativelyPrime(i, phiN)):
            e = i
            break
    return e

def getD(e, phiN):
    return modInverse(e, phiN)

def main():
    p, q = getTwoPrimes(200)
    n = p * q
    resultPhiN = phi(p, q)
    e = getE(resultPhiN)
    d = getD(e, resultPhiN)

    publicKey = [e, n]
    privateKey = [d, n]

    print(publicKey)
    print(privateKey)

    plainText = "No class for today"
    asciiPlainText = textToAscii(plainText)
    print(asciiPlainText)

    # Encrypt
    asciiCipherText = []
    for i in asciiPlainText:
        asciiCipherText.append(power(i, e, n))

    print(asciiCipherText)

    cipherText = asciiToText(asciiCipherText) 
    print(str(cipherText))

    # Decrypt
    asciiDecrypted = []
    for i in asciiCipherText:
        asciiDecrypted.append(power(i, d, n))

    print(asciiDecrypted)
    print(asciiToText(asciiDecrypted))

if __name__ == "__main__":
    main()