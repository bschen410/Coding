def dfs(path: list, target, road: set):
    if path[-1] == target:
        yield path
    for i in road:
        tmp = set(i) - {path[-1]}
        if len(tmp) == 2:
            continue
        end = tmp.pop()
        if end not in path:
            yield from dfs(path + [end], target, road)


def main():
    n, source, target = input().split()
    rest = input().split()
    road = set()
    for _ in range(int(n)):
        road.add(frozenset(input().split()))
    result = dfs([source], target, road)
    result = [i for i in result if set(rest) & set(i)]
    if result:
        min_path = min(result, key=len)
        print((set(min_path) & set(rest)).pop())
        print(" ".join(min_path))
    else:
        print("NO")


if __name__ == "__main__":
    main()
