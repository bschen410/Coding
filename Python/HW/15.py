
def common(data):
    max_times = 0
    max_value = 0
    for i in range(len(data)):
        if data.count(data[i]) > max_times:
            max_times = data.count(data[i])
            max_value = data[i]
    return max_value

n = int(input())
data = [list(map(float, input().split())) for _ in range(n)]
for i in range(n): data[i].append(round(data[i][1] / data[i][0] / data[i][0], 2))

data.sort(key=lambda x: x[2])
# print(data)
# print(len(data))

print('%.2f'%max(data, key=lambda x: x[2])[2])

print('%.2f'%min(data, key=lambda x: x[2])[2])

if len(data) % 2:
    print(data[len(data) // 2][2])
else:
    print('%.2f'%(round((data[n // 2 - 1][2] + data[n // 2][2]) / 2, 2) - 0.01))

print(common([data[_][2] for _ in range(n)]))
