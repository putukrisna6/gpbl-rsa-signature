from asyncio.windows_events import NULL

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

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def relativelyPrime(e, phi):
    return gcd(e, phi) == 1

def modInverse(a, m):
    g, x, y = egcd(a, m)
    return x % m