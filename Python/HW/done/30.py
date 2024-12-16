def C(n, t):
    if n == 0 or n == 1:
        t += 1
        return t - 1
    if n % 2:
        t += 1
        return C((n + 1) / 2, t)
    else:
        t += 1
        return C(n / 2, t)


def main():
    while True:
        inp = input()
        if inp == "-1":
            break
        res = 0
        for i in range(int(inp, 2) + 1):
            res += C(i, 0)
        print(format(res, "014b"))


if __name__ == "__main__":
    main()
