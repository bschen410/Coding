def dfs(path: list, target, data, value=0):
    if path[-1] == target:
        yield path, value
    for i in data[path[-1]]:
        if i["friend"] not in path:
            for j in data[i["friend"]]:
                if j["friend"] == path[-1]:
                    min_value = min(i["value"], j["value"])
                    yield from dfs(path + [i["friend"]], target, data, value + min_value)


def main():
    n = int(input())
    source = "A"
    target = "B"
    data = {}
    while True:
        inp = input().split()
        if inp[0] == "-1":
            break
        if inp[0] not in data:
            data[inp[0]] = [{"friend": inp[1], "value": int(inp[2])}]
        else:
            data[inp[0]].append({"friend": inp[1], "value": int(inp[2])})
    result = list()
    for res in dfs([source], target, data):
        result.append(res)
    print(len(min(result, key=lambda x: x[1])[0]) - 1)
    print(" ".join(min(result, key=lambda x: x[1])[0]))
    print(max(result, key=lambda x: x[1])[1])
    print(" ".join(max(result, key=lambda x: x[1])[0]))


if __name__ == "__main__":
    main()
