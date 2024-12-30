def dfs(data, start, total, path: list):
    index = next((i for i, item in enumerate(data) if item["id"] == start), None)
    for d in data[index]["conn"]:
        # print("start:", start, "path:", path, "total:", total)
        if d == 0 or d in path:
            # print("  result:", total, path, start)
            yield total
        else:
            idx = next((i for i, item in enumerate(data) if item["id"] == d), None)
            yield from dfs(data, d, total + data[idx]["value"], path + [d])
    return "-1"


def main():
    n, entry = map(int, input().split())
    data = []
    for _ in range(n):
        inp = list(map(int, input().split()))
        data.append({"id": inp[0], "value": inp[1], "conn": [inp[2], inp[3]]})
    entry_idx = next((i for i, item in enumerate(data) if item["id"] == entry), None)
    result = dfs(data, entry, data[entry_idx]["value"], [entry])
    print(max(list(result)))


if __name__ == "__main__":
    main()
