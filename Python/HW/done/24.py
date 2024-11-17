def convertCardPoint(str):
    if str >= "2" and str <= "9":
        return int(str)
    elif str == "10":
        return 10
    elif str == "A":
        return 1
    elif str == "J" or str == "Q" or str == "K":
        return 0.5
    return -1


def main():
    n = int(input())
    bet = [int(x) for x in input().split()]
    firstCard = [convertCardPoint(x) for x in input().split()]
    score = [[firstCard[i]] for i in range(n + 1)]
    for i in range(1, n + 1):
        # print("i =", i)
        while True:
            inp = input().split()
            if inp[0] == "Y":
                score[i].append(convertCardPoint(inp[1]))
            elif inp[0] == "N":
                break
            if sum(score[i]) > 10.5:
                bet[i - 1] = -bet[i - 1]
                break
            elif sum(score[i]) == 10.5:
                # 電腦立賠
                break
    # print("!!!")
    # print(score)
    #
    allBoom = True
    for i in range(n):
        if bet[i] > 0:
            allBoom = False
            break
    pointSum = [sum(score[i]) for i in range(1, n + 1)]
    if set(pointSum) == {10.5} or allBoom:
        # print("!!!有人抱了???")
        for i in range(n):
            if bet[i] > 0:
                print("Player%d +%d" % (i + 1, bet[i]))
            else:
                print("Player%d %d" % (i + 1, bet[i]))
        if sum(bet) > 0:
            print("Computer %d" % (-sum(bet)))
        else:
            print("Computer +%d" % (-sum(bet)))
        exit()
    #
    # minScore = min(sum(score[1 : n + 1])) if min(sum(score[1 : n + 1])) <= 10.5 else 0
    minScore = 99
    for i in range(1, n + 1):
        if sum(score[i]) <= 10.5 and sum(score[i]) < minScore:
            minScore = sum(score[i])
    while True:
        if sum(score[0]) <= minScore and not sum(score[0]) == 10.5:
            score[0].append(convertCardPoint(input()))
        else:
            break
        if sum(score[0]) > 10.5:
            score[0] = [-1]
            break
    # output
    for i in range(n):
        if sum(score[i + 1]) <= sum(score[0]) and sum(score[i + 1]) != 10.5:
            bet[i] = -bet[i]
        if bet[i] > 0:
            print("Player%d +%d" % (i + 1, bet[i]))
        else:
            print("Player%d %d" % (i + 1, bet[i]))
    if sum(bet) > 0:
        print("Computer %d" % (-sum(bet)))
    else:
        print("Computer +%d" % (-sum(bet)))
    exit()


if __name__ == "__main__":
    main()
