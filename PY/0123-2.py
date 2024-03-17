start = int(input("Start: "))
end = int(input("End: "))
t = 1
for i in range (start, end):
    for j in range (2, i-1):
        if i % j == 0:
            t = 0
            break
    if t == 1 and i != 1:
        print(i, " ")
    elif t == 0:
        t = 1
exit()
