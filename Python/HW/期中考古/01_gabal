def type1(rows):
    for r in range(rows):
        output = str(r + 1) * (r + 1)
        print(output.ljust(rows, "#"))


def minManMin(n):
    left = ""
    right = ""
    for i in range(1, n):
        left += str(i)
        right += str(n - i)
    return left + str(n) + right


def type2(rows):
    for r in range(rows):
        print(minManMin(r + 1).rjust(rows * 2 - 1, "#"))


def minMax(n):
    left = ""
    for i in range(n):
        left += str(i + 1)
    return left


def maxMin(n):
    right = ""
    for i in range(n - 1, -1, -1):
        right += str(i + 1)
    return right


def type3(rows):
    for r in range(rows):
        print(minMax(r + 1).ljust(rows, "^"))
    for r in range(rows - 1, -1, -1):
        print(maxMin(r + 1).ljust(rows, "^"))


def maxMinMax(n):
    left = ""
    for r in range(n, 0, -1):
        left += str(r)
    right = ""
    for r in range(2, n + 1):
        right += str(r)
    return left + right


def type4(rows):
    for r in range(1, rows):
        output = maxMinMax(r)
        print(output.center(2 * rows - 1, "^"))
    for r in range(rows, 0, -1):
        output = maxMinMax(r)
        print(output.center(2 * rows - 1, "^"))


type4(6)
