a, b = input().split()
a, b = int(a), int(b)
for i in range(min(a, b), 1, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        exit()

