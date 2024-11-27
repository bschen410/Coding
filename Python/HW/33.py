from itertools import combinations


def main():
    n = int(input())
    drone = [list(map(int, input().split())) for _ in range(n)]
    dist = list()
    for i in combinations(range(n), 2):
        dist.append(
            [
                i[0],
                i[1],
                (
                    (drone[i[0]][1] - drone[i[1]][1]) ** 2
                    + (drone[i[0]][2] - drone[i[1]][2]) ** 2
                    + (drone[i[0]][3] - drone[i[1]][3]) ** 2
                )
                ** 0.5,
            ]
        )
    dist.sort(key=lambda x: x[2])
    for i in range(3):
        print(
            drone[dist[i][0]][0],
            drone[dist[i][1]][0],
            drone[dist[i][0]][1],
            drone[dist[i][0]][2],
            drone[dist[i][0]][3],
            drone[dist[i][1]][1],
            drone[dist[i][1]][2],
            drone[dist[i][1]][3],
        )


if __name__ == "__main__":
    main()
