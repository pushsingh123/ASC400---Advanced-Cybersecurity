def isPrime(a):
    if (a < 2):
        return False
    for i in range(2, a):
        if (a % i == 0):
            return False
    return True

def getGCD(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = getGCD(b % a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y

def isRelativePrime(a, b):
    if (getGCD(a, b)[0] == 1):
        return True
    return False

def getModularInverse(n, b):
    gcd, x, y = getGCD(n,b)
    if (gcd == 1):
        return y % n
    return "None found"

def checkPhi(n):
    list = []
    for i in range(1, n+1):
        if (isRelativePrime(i,n)):
            list.append(i)
    return list


if __name__ == "__main__":
    print(checkPhi(9))