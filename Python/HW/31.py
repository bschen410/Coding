def G(n, k, res):
    if n == 0:
        # res += str(k)
        return res
    elif k < 2 ** (n - 1):
        res += "0"
        return G(n - 1, k, res)
    elif k >= 2 ** (n - 1):
        res += "1"
        return G(n - 1, 2**n - 1 - k, res)


def main():
    while True:
        try:
            res = ""
            n, k = map(int, input().split())
            print(G(n, k, res))
        except ValueError:
            break


if __name__ == "__main__":
    main()
