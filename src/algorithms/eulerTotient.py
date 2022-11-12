from helper.calculations import gcd

def phi(n):
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result += 1
    return result

def phi(p, q):
    return (p-1)*(q-1)