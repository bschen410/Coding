def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

a = 12
b = 18
result = gcd(a, b)
print("The greatest common divisor of", a, "and", b, "is", result)
