import re

def isError(card):
    for value in card:
        if re.match(r'^[2-9AJQK][SHDC]$', value) == None and \
           re.match(r'^[1][0][SHDC]$', value) == None:
            return True
    return False

def checkCardType(values, suits):
    values = sorted(values)
    # 5 6 9
    isStraight = False
    diff = set()
    for i in range(len(values)-1): diff.add(values[i+1] - values[i])
    if diff == {1} or diff == {1, 9}: isStraight = True
    isSameSuits = True if suits.count(suits[0]) == len(suits) else False
    if isStraight and isSameSuits: return '9' # Straight Flush
    elif isStraight: return '5' # Straight
    elif isSameSuits: return '6' # Flush
    # 8 7 4
    valueCountSet = {values.count(i) for i in values}
    if max(valueCountSet) == 4: return '8' # Four of a kind
    elif max(valueCountSet) == 3:
        if valueCountSet == {2, 3}: return '7' # Full House
        else: return '4' # Three of the kind
    # 3 2 1
    valueCountList = [values.count(i) for i in values]
    if valueCountList.count(2) == 4: return '3' # Two pairs
    elif valueCountList.count(2) == 2: return '2' # One pair
    else: return '1' # High Card

def main():
    n = int(input())
    result = list()
    allCard = list()
    for _ in range(n):
        inp = input().split()
        card = inp[1:]
        if isError(card):
            print('Error input')
            exit()
        for i in card:
            allCard.append(i)
            if allCard.count(i) > 1:
                print('Duplicate deal')
                exit()
        # Convert card list to cardValues and cardSuits
        cardValues = list()
        cardSuits = list()
        for i in range(len(card)):
            if card[i][0] == 'A': cardValues.append(1)
            elif card[i][0] == 'J': cardValues.append(11)
            elif card[i][0] == 'Q': cardValues.append(12)
            elif card[i][0] == 'K': cardValues.append(13)
            elif card[i][0] == '1' and card[i][1] == '0':
                cardValues.append(10)
                cardSuits.append(card[i][2])
                continue
            else: cardValues.append(int(card[i][0]))
            cardSuits.append(card[i][1])
        #
        result.append([inp[0], checkCardType(cardValues, cardSuits)])
    result = sorted(result, key=lambda x : x[1], reverse=True)
    for i in result: print(i[0], i[1])

if __name__ == '__main__':
    main()
