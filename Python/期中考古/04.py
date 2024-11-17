lesson = list()


def isConflict(x, y):
    for i in range(len(lesson[x]["time"])):
        for j in range(len(lesson[y]["time"])):
            if lesson[x]["time"][i] == lesson[y]["time"][j]:
                print(
                    lesson[x]["name"],
                    "and",
                    lesson[y]["name"],
                    "conflict on",
                    lesson[x]["time"][i],
                )


def main():
    n = int(input())
    for i in range(n):
        lesson.append(dict())
        lesson[i]["name"] = input()
        t = int(input())
        lesson[i]["time"] = [input() for _ in range(t)]
    # print(lesson)
    for i in range(n - 1):
        for j in range(i + 1, n):
            isConflict(i, j)


main()

# 15 min
