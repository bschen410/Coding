import math


def calculate(n, m, sicknow, b, c, d, time, plus):
    maxsickpeople = int(n * (1 - d))
    if m > time:
        return 0
    if m > c:
        healthpeople = sickpeople[m - c - 1]
    else:
        healthpeople = 0
    if sicknow + plus > maxsickpeople:
        plus = maxsickpeople - sicknow
    if plus < 0:
        plus = 0
    sickpeople.append(plus)
    sicknow = sicknow + plus - healthpeople
    print(f"{m} {sicknow} {plus} {healthpeople}")

    d = d + healthpeople / n
    x = (b / c) * (1 - d)
    y = math.floor(sicknow * x)
    return calculate(n, m + 1, sicknow, b, c, d, time, y)


def main():
    totalpeople, time, firstday, spread, day, health = [eval(input()) for _ in range(6)]
    calculate(totalpeople, 1, 0, spread, day, health, time, firstday)
    print(sum(sickpeople))


sickpeople = list()
main()
