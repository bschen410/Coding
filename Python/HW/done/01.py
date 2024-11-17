stdName = input()
stdID = input()
stdScore = []
sum = 0
for i in range(3):
    tmp = int(input())
    stdScore.append(tmp)
    sum += stdScore[i]
print('Name:' + stdName)
print('ID:' + stdID)
print('%s%d'%('Average:', sum / 3))
print('%s%d'%('Total:', sum))
