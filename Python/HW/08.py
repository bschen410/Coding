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
        for j in range (t):
            timeOfLesson[i][j] = input()
    isConflict(0, 1)
    isConflict(0, 2)
    isConflict(1, 2)
    if isAC == True:
        print('correct')

main()

# timeOfLesson = dict()
# isAC = True
# 
# def isConflict(x, y):
#     for i in range (len(timeOfLesson[x])):
#         for j in range (len(timeOfLesson[y])):
#             if timeOfLesson[x][i] == timeOfLesson[y][j]:
#                 print(timeOfLesson[x]['sbjName'], timeOfLesson[y]['sbjName'], timeOfLesson[x][i], sep = ",")
#                 isAC = False
# 
# def main():
#     for i in range (3):
#         s = input()
#         t = int(input())
#         for j in range (t):
#             timeOfLesson[i] = {j: input(), 'sbjName': s}
#     isConflict(0, 1)
#     isConflict(1, 2)
#     isConflict(0, 2)
#     if isAC == True:
#         print('correct')
# 
# main()
# 
# 
# 
# 
# # try:
# # except: