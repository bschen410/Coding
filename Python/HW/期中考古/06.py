cards = list()


def convert(s):
    table = ["A"] + [str(i) for i in range(2, 11)]
    if s in table:
        return table.index(s) + 1
    elif s in ["J", "Q", "K"]:
        return 0.5


def play(card):
    while True:
        if card > 10.5:
            return card
        elif card == 10.5:
            return card
        inp = input().split()
        if inp[0] == "Y":
            card += convert(inp[1])
        elif inp[0] == "N":
            break
    return card


def main():
    n = int(input())
    bet = [0]
    bet.extend(input().split())
    bet = [int(bet[i]) for i in range(len(bet))]
    inp = input().split()
    cards = [convert(inp[i]) for i in range(n + 1)]
    for i in range(1, n + 1):
        cards[i] = play(cards[i])
    minPoint = min(cards[1:])
    while cards[0] < minPoint:
        if cards[0] > 10.5:
            break
        cards[0] += int(input())
    #
    for i in range(1, n + 1):
        if cards[i] <= cards[0] and cards[0] <= 10.5 and not cards[i] == 10.5:
            bet[i] = -bet[i]
    for i in range(1, n + 1):
        if bet[i] > 0:
            print("Player%d +%d" % (i, bet[i]))
        else:
            print("Player%d %d" % (i, bet[i]))
    # bet[0] = -(sum(bet))


main()

# 52 min
