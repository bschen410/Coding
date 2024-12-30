def cal_pts(playerA, check, n):
    pts = 0
    table = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if playerA[i][j] in check:
                table[i][j] = 1
    for i in range(n):
        if all(table[i]):
            pts += 1
    for i in range(n):
        if all([table[j][i] for j in range(n)]):
            pts += 1
    if all([table[i][i] for i in range(n)]):
        pts += 1
    if all([table[i][n - i - 1] for i in range(n)]):
        pts += 1
    return pts


def main():
    n, m = int(input()), int(input())
    inp = list(map(int, input().split()))
    playerA = [inp[i * n : i * n + n] for i in range(n)]
    inp = list(map(int, input().split()))
    playerB = [inp[i * n : i * n + n] for i in range(n)]
    check = list(map(int, input().split()))
    A_pts = cal_pts(playerA, check, n)
    B_pts = cal_pts(playerB, check, n)
    if A_pts > B_pts:
        print("A Win")
    elif A_pts < B_pts:
        print("B Win")
    else:
        print("Tie")


if __name__ == "__main__":
    main()
