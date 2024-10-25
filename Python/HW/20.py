def turnLeft(m, n):
    new = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new[i][j] = m[j][n-i-1]
    return new

def turnRight(m, n):
    new = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new[i][j] = m[n-j-1][i]
    return new

def main():
    n = int(input())
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        matrix[i] = [i + 1 for i in range(i * n, i * n + n)]
    s = input()
    dir = 0
    for i in s:
        if i == 'L': dir += 1
        elif i == 'R': dir -= 1
    # print(f"dir: {dir}")
    if dir > 0:
        for i in range(dir):
            matrix = turnLeft(matrix, n)
    elif dir < 0:
        for i in range(abs(dir)):
            matrix = turnRight(matrix, n)
    # else:
    #     matrix = [[matrix[i][j] for j in range(n)] for i in range(n)]
    # print(newMatrix)
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()

if __name__ == '__main__':
    main()
