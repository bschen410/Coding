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
    isPlayerChk = True
    isComputerChk = True
    playerScore = [convertCardPoint(input())]
    computerScore = [convertCardPoint(input())]
    while True:
        if isPlayerChk:
            inp = input()
            if inp == "Y":
                playerScore.append(convertCardPoint(input()))
            elif inp == "N":
                isPlayerChk = False
        # check if player boom
        if sum(playerScore) > 10.5:
            print("computer win")
            exit()
        if isComputerChk and (
            sum(computerScore) < sum(playerScore) or sum(computerScore) <= 8
        ):
            computerScore.append(convertCardPoint(input()))
        else:
            isComputerChk = False
        # 判斷輸贏
        if sum(computerScore) > 10.5:
            print("player win")
            exit()
        if not (isPlayerChk or isComputerChk):
            if sum(playerScore) > sum(computerScore):
                print("player win")
            elif sum(playerScore) < sum(computerScore):
                print("computer win")
            else:
                print("it's a tie")
            exit()


if __name__ == "__main__":
    main()
