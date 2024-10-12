import math

a = int(input())
b = int(input())
c = int(input())
if b*b-4*a*c >= 0:
    x1 = ((-b) + math.sqrt(b*b-4*a*c)) / (2*a)
    x2 = ((-b) - math.sqrt(b*b-4*a*c)) / (2*a)
    print("%.1f" %x1)
    print("%.1f" %x2)
