start = input(int)
end = input(int)
for i in range (start, end):
    for j in range (2, i-1):
        if i % j == 0:
            print(j, " ")
        break
exit()