data = dict()


def dfs(path: list, target, value=0):
    if path[-1] == target:
        yield value
    for i in data[path[-1]]:
        print(i)
        # if i not in path:
        #     yield from dfs(path + [i], target, value + i["value"])


def main():
    n = int(input())
    source = "A"
    target = "B"
    while True:
        inp = input().split()
        if inp[0] == "-1":
            break
        if inp[0] in data:
            data[inp[0]]["friend"].append(inp[1])
            data[inp[0]]["value"].append(int(inp[2]))
        else:
            data.update({inp[0]: {"friend": [inp[1]], "value": [int(inp[2])]}})
    print(data)
    for result in dfs([source], target):
        print(result)


if __name__ == "__main__":
    main()
