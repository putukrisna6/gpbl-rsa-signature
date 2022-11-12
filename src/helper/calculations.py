def power(x, y, p):
    result = 1
    x %= p

    while (y > 0):
        if (y & 1):
            result = (result * x) % p

        y = y >> 1
        x = (x * x) % p
    return result

def gcd(a, b):
    while(b > 0):
        r = a % b
        a = b
        b = r
    return a

def relativelyPrime(e, phi):
    return gcd(e, phi) == 1