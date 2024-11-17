score =  list()

def func(firstBall, secondBall, flag):
    if flag == 1:
        firstBall *= 2
        secondBall *= 2
    elif flag == 2:
        firstBall *= 2
    #
    if secondBall == 0:
        score.append([firstBall])
        return
    else:
        score.append([firstBall, secondBall])
        return
    # print('a:', firstBall, secondBall)


def main():
    flag = 0
    for _ in range(10):
        firstBall = int(input())
        secondBall = int()
        if firstBall != 10:
            secondBall = int(input())
        # 0: normal, 1: strike, 2: spare
        func(firstBall, secondBall, flag)
        if firstBall == 10: flag = 1
        elif firstBall + secondBall == 10: flag = 2
        else: flag = 0
    #
    totalScore = 0
    if flag == 1: totalScore += (int(input()) + int(input()))
    elif flag == 2: totalScore += int(input())
    totalScore += sum(sum(inner) for inner in score)
    print(totalScore)

if __name__ == '__main__':
    main()
