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
        res = C(int(input(), 2), 0)
        print(format(res, "08b"))
        if input() == "-1":
            break


if __name__ == "__main__":
    main()
