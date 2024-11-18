import re


def first(a, b):
    return a + " " + b


def second(c, x, y):
    c_split = c.split()
    for i in range(len(c_split)):
        if c_split[i].upper() == x.upper():
            c_split[i] = y
    return " ".join(c_split)


def fifth(c, n):
    res = ""
    for i in range(0, len(c), n):
        # if c[i] == " " and res[-1] == " ":
        #     continue
        res += c[i]
    return res


def main():
    a = input()
    b = input()
    x = input()
    y = input()

    c = first(a, b)
    print(c)

    # d = c.replace(x, y)
    d = second(c, x, y)
    print(d)

    print(len(c) - c.count(" "), len(d) - d.count(" "))

    print(d.replace(y, "".join(reversed(y))))

    n = abs(len(x) - len(y))
    print(fifth(c, n))


if __name__ == "__main__":
    main()
