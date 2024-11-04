def f1(n):
    m = [[0] * n for _ in range(n)]
    num = n
    for i in range(n):
        for j in range(n):
            m[i][j] = num + j * n
        num -= 1
    return m


def f2(n):
    m = [[0] * n for _ in range(n)]
    num = 1
    for i in range(n - 1, -1, -1):
        for j in range(n):
            m[j][i] = num
            num += 1
    return m


def f3(n):
    m = [[0] * n for _ in range(n)]
    num = 1
    for i in range(n - 1, -1, -1):
        for j in range(n):
            m[i][j] = num
            num += 1
    return m


def f4(n):
    m = [[0] * n for _ in range(n)]
    num = 1
    for i in range(n):
        for j in range(n - 1, -1, -1):
            m[i][j] = num
            num += 1
    return m


def main():
    n = int(input())
    d = int(input())
    if d == 1:
        m = f1(n)
    elif d == 2:
        m = f2(n)
    elif d == 3:
        m = f3(n)
    elif d == 4:
        m = f4(n)
    # print(m)
    for i in range(n):
        for j in range(n):
            print("%3d" % m[i][j], end="")
        print()


main()

# 18 min
