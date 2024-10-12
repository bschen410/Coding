timeOfLesson = dict()
isAC = True

def isConflict(x, y):
    global isAC
    for i in range (len(timeOfLesson[x]) - 1):
        for j in range (len(timeOfLesson[y]) - 1):
            if timeOfLesson[x][i] == timeOfLesson[y][j]:
                print(timeOfLesson[x]['sbjName'], timeOfLesson[y]['sbjName'], timeOfLesson[x][i], sep = ",")
                isAC = False

def main():
    global isAC
    for i in range (3):
        s = input()
        timeOfLesson[i] = {'sbjName': s}
        # code below also works
        # timeOfLesson[i] = {}
        # timeOfLesson[i]['sujName'] = 'test'
        t = int(input())
        if t < 1 or t > 3:
            print('-1')
            return
        for j in range (t):
            inp = input()
            if (not(inp[0] >= '1' and inp[0] <= '5') or
                not(inp[1] >= '1' and inp[1] <= '9') and
                not(inp[1] >= 'a' and inp[1] <= 'c')):
                print('-1')
                return
            timeOfLesson[i][j] = inp
    isConflict(0, 1)
    isConflict(0, 2)
    isConflict(1, 2)
    if isAC == True:
        print('correct')

main()