mtx = [list(map(int, input().split())) for _ in range(4)]
m = [mtx[0 + i][2 + j] for i in range(1) for j in range(1)]
print(m)
