def getZeroIndex(mtx):
    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            if mtx[i][j] == 0:
                return i, j
    return False


def checkRow(mtx):
    for row in range(4):
        nums = {i for i in range(1, 5)}
        m = mtx[row]
        if m.count(0) == 1:
            zeroIndex = m.index(0)
            nums -= set(m)
            mtx[row][zeroIndex] = nums.pop()
    return mtx


def checkCol(mtx):
    for col in range(4):
        nums = {i for i in range(1, 5)}
        m = [mtx[row][col] for row in range(4)]
        if m.count(0) == 1:
            zeroIndex = m.index(0)
            nums -= set(m)
            mtx[zeroIndex][col] = nums.pop()
    return mtx


def checkBlk(mtx):
    pos = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for x, y in pos:
        nums = {i for i in range(1, 5)}
        m = [mtx[x + i][y + j] for i in range(2) for j in range(2)]
        if m.count(0) == 1:
            zeroIndex = m.index(0)
            nums -= set(m)
            mtx[x + zeroIndex // 2][y + zeroIndex % 2] = nums.pop()
    return mtx


def main():
    mtx = [list(map(int, input().split())) for _ in range(4)]
    while getZeroIndex(mtx):
        mtx = checkRow(mtx)
        mtx = checkCol(mtx)
        mtx = checkBlk(mtx)
    for i in range(4):
        for j in range(4):
            print(mtx[i][j], end=" ")
        print()


if __name__ == "__main__":
    main()
