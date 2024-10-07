lst = [False] * 50
count = 0

for i in range (3):
    x = int(input())
    y = int(input())
    if x < -20 or x > 20 or y < -20 or y > 20:
        print('-1')
        exit()
    for j in range (x + 20, y + 20):
        lst[j] = True

for i in range (len(lst)):
    if lst[i] == True:
        try:
            count += 1
            i += 1
        except lst[i] == False:
            pass

print(count)