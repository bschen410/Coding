def convertFactors(inp):
    for i in inp:
        if i == "+":
            return [inp[: inp.index(i)]] + convertFactors(inp[inp.index(i) + 1 :])
    return [inp]


def conformAll(data, factors):
    for ftr in factors:
        output = []
        for d in data:
            for f in ftr:
                if set(f).issubset(set(d["prop"])):
                    output.append(d["name"])
                    break
        print(" ".join(output))


def conformMost(data, factors):
    count = [[0] * len(data) for _ in range(len(factors))]
    for factor in factors:
        for d in data:
            for ftr in factor:
                for f in ftr:
                    if f in d["prop"]:
                        count[factors.index(factor)][data.index(d)] += 1
    for i in count:
        for j in range(len(i)):
            if i[j] == max(i):
                print(data[j]["name"], end=" ")
        print()


def main():
    n = int(input())
    data = []
    for _ in range(n):
        inp = input().split()
        data.append({"name": inp[0], "prop": inp[1:]})
    # print(data)
    m = int(input())
    factors = [convertFactors(input().split()) for _ in range(m)]
    # print(factors)
    if input() == "0":
        conformAll(data, factors)
    else:
        conformMost(data, factors)


if __name__ == "__main__":
    main()
