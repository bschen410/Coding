import re

n = 2
m = 5


def chkError(card):
    for i in range(n):
        for j in range(m):
            if len(card[i][j]) == 3:
                if re.match(r"[1][0][SHDC]", card[i][j]) == None:
                    print("Error input")
                    exit()
            elif len(card[i][j]) == 2:
                if re.match(r"[2-9JQKA][SHDC]", card[i][j]) == None:
                    print("Error input")
                    exit()
            else:
                print("Error input")
                exit()
    plus = card[0] + card[1]
    if len(set(plus)) != len(plus):
        print("Duplicate deal")
        exit()
    # for i in range(n):
    #     if len(set(card[i])) != len(card[i]):


def cvtCardPt(str):
    if str[0] == "1":
        s = "10"
    else:
        s = str[0]
    ptTable = ["0", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    return ptTable.index(s)


def calCardType(card):
    typeChk = list()
    isStraight = False
    isSameSuit = False
    chkStraight = set()
    cardNum = [cvtCardPt(card[i]) for i in range(m)]
    cardNum.sort()
    numCount = [cardNum.count(i) for i in cardNum]
    for i in range(m - 1, 0, -1):
        chkStraight.add(cardNum[i] - cardNum[i - 1])
    if chkStraight == {1} or chkStraight == {1, 9}:
        isStraight = True
    chkSuit = set()
    for i in range(m):
        chkSuit.add(card[i][-1])
    if len(chkSuit) == 1:
        isSameSuit = True
    #
    if isStraight and isSameSuit:
        typeChk.append(9)  # Straight flush
    elif isSameSuit:
        typeChk.append(6)  # Flush
    elif isStraight:
        typeChk.append(5)  # Straight
    #
    if set(numCount) == {1, 4}:
        typeChk.append(8)  # Four of a king
    elif set(numCount) == {2, 3}:
        typeChk.append(7)  # Full house
    elif set(numCount) == {1, 3}:
        typeChk.append(4)  # Three of a king
    elif set(numCount) == {1, 2}:
        if numCount.count(2) == 4:
            typeChk.append(3)  # Two pairs
        typeChk.append(2)  # One pair
    else:
        typeChk.append(1)  # High card
    #
    return max(typeChk)


def main():
    inp = [input().split() for _ in range(n)]
    chkError(inp)
    print(max(calCardType(inp[0]), calCardType(inp[1])))
    # print(calCardType(inp[0]), calCardType(inp[1]))


main()

# more than 1 hour
