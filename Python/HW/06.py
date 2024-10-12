import math
import cmath

a, b, c = int(input()), int(input()), int(input())
t = b * b - 4 * a * c

if (t >= 0):
    T = math.sqrt(b * b - 4 * a * c)
    x1 = (-b + T) / (2 * a)
    x2 = (-b - T) / (2 * a)
    print("%.1f"%(x1))
    print("%.1f"%(x2))
else:
    T2 = cmath.sqrt(b * b - 4 * a * c)
    x1 = (-b + T2) / (2 * a)
    x2 = (-b - T2) / (2 * a)
    print("%.1f+%.1fi" %(x1.real, x1.imag))
    print("%.1f%.1fi" %(x2.real, x2.imag))
