def check_point(mat: list, side: int):
    point = 0
    point2 = 0
    for i in range(side):
        if all(mat[i::side]):
            point += 1
            point2 += sum(mat[i::side])
        if all(mat[i * side : i * side + side]):
            point += 1
            point2 += sum(mat[i * side : i * side + side])
    if all(mat[i * side + i] for i in range(side)):
        point += 1
        point2 += sum(mat[i * side + i] for i in range(side))
    if all(mat[i * side - i] for i in range(1, side + 1)):
        point += 1
        point2 += sum(mat[i * side - i] for i in range(1, side + 1))
    return point, point2


def main():
    mat_side = int(input())
    circles = int(input())
    mat_a = input().split()
    mat_b = input().split()
    circled = input().split()

    mat_a = [int(n) if n in circled else 0 for n in mat_a]
    mat_b = [int(n) if n in circled else 0 for n in mat_b]
    score_a, score_a2 = check_point(mat_a, mat_side)
    score_b, score_b2 = check_point(mat_b, mat_side)
    if score_a > score_b:
        print("A Win")
    elif score_a < score_b:
        print("B Win")
    else:
        if score_a2 > score_b2:
            print("A Win")
        elif score_a2 < score_b2:
            print("B Win")
        else:
            print("Tie")


if __name__ == "__main__":
    main()
