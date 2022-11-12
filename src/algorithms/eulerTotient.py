from helper.calculations import egcd

def phi(n):
    result = 1
    for i in range(2, n):
        g, x, y = egcd(10, 15)
        if (g == 1):
            result += 1
    return result

def phi(p, q):
    return (p-1)*(q-1)