lst = [False] * 50
count = 0

time = int(input())
for i in range(time):
    inp = input().split()
    inp = [int(i) for i in inp]
    for j in range(inp[0] + 20, inp[1] + 20):
        lst[j] = True

for i in range (len(lst)):
    if lst[i] == True:
        count += 1
# count = lst.count(True)

print(count)
