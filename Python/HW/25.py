import re
from itertools import combinations


def isError(card):
    for value in card:
        if (
            re.match(r"^[SHDC][2-9AJQK]$", value) == None
            and re.match(r"^[SHDC][1][0]$", value) == None
        ):
            return True
    return False


def checkCardType(values, suits):
    values = sorted(values)
    # 5 6 9
    isStraight = False
    diff = set()
    for i in range(len(values) - 1):
        diff.add(values[i + 1] - values[i])
    if diff == {1} or diff == {1, 9}:
        isStraight = True
    isSameSuits = True if suits.count(suits[0]) == len(suits) else False
    if isStraight and isSameSuits:
        return "9"  # Straight Flush
    elif isStraight:
        return "5"  # Straight
    elif isSameSuits:
        return "6"  # Flush
    # 8 7 4
    valueCountSet = {values.count(i) for i in values}
    if max(valueCountSet) == 4:
        return "8"  # Four of a kind
    elif max(valueCountSet) == 3:
        if valueCountSet == {2, 3}:
            return "7"  # Full House
        else:
            return "4"  # Three of the kind
    # 3 2 1
    valueCountList = [values.count(i) for i in values]
    if valueCountList.count(2) == 4:
        return "3"  # Two pairs
    elif valueCountList.count(2) == 2:
        return "2"  # One pair
    else:
        return "1"  # High Card


def main():
    player_a = input().split()
    player_b = input().split()
    share_card = input().split()
    combined = player_a + player_b + share_card
    assemble = [player_a, player_b, share_card]
    if isError(player_a) or isError(player_b) or isError(share_card):
        print("Error input")
        exit()
    for i in combined:
        if combined.count(i) > 1:
            print("Duplicate deal")
            exit()
    # Convert card list to cardValues and cardSuits
    res = [0, 0]
    card_and_value = {str(n): n for n in range(2, 11)}
    card_and_value.update({"A": 1, "J": 11, "Q": 12, "K": 13})
    for i in range(2):
        random = assemble[i] + assemble[2]
        for c in combinations(random, 5):
            cardValues = list()
            cardSuits = list()
            for n in c:
                cardValues.append(card_and_value[n[1:]])
            for n in range(5):
                cardSuits.append(c[n][0])
            if int(checkCardType(cardValues, cardSuits)) > res[i]:
                res[i] = int(checkCardType(cardValues, cardSuits))
                # print(res[i], i)
    # Compare the result
    if res[0] > res[1]:
        print("A", res[0])
    elif res[0] < res[1]:
        print("B", res[1])
    else:
        print("Tie")


if __name__ == "__main__":
    main()
