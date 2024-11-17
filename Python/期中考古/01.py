def g1(n):
    for i in range(1, n + 1):
        print(str(i) * i, end="")
        print("#" * (n - i))


def g2(n):
    for i in range(1, n + 1):
        s = ""
        for j in range(1, i + 1):
            s += str(j)
        for j in range(i - 1, 0, -1):
            s += str(j)
        print(s.rjust(2 * 5 - 1, "#"))


def g3(n):
    for i in range(1, n + 1):
        s = ""
        for j in range(1, i + 1):
            s += str(j)
        print(s.ljust(n, "^"))
    for i in range(n, 0, -1):
        s = ""
        for j in range(i, 0, -1):
            s += str(j)
        print(s.ljust(n, "^"))


def g4(n):
    for i in range(1, n + 1):
        s = ""
        for j in range(i, 0, -1):
            s += str(j)
        for j in range(2, i + 1):
            s += str(j)
        print(s.center(2 * n - 1, "^"))
    for i in range(n - 1, 0, -1):
        s = ""
        for j in range(i, 0, -1):
            s += str(j)
        for j in range(2, i + 1):
            s += str(j)
        print(s.center(2 * n - 1, "^"))


def main():
    inp = int(input())
    if inp == 1:
        g1(int(input()))
    elif inp == 2:
        g2(int(input()))
    elif inp == 3:
        g3(int(input()))
    elif inp == 4:
        g4(int(input()))


main()


# 41 min
# 15 -> 51
