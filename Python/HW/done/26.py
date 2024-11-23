def main():
    ppl, period, case, rate, rcvDay, immRate = [eval(input()) for _ in range(6)]
    rcvCase = [0 for _ in range(period * 2)]
    caseCount = 0
    for day in range(1, period + 1):
        newCase = int(case * (rate / rcvDay) * (1 - immRate))
        if day == 1:
            newCase = case
        else:
            if ppl * (1 - immRate) < (case + newCase):
                newCase = round(ppl * (1 - immRate)) - case
            case += newCase
        if rcvCase[day - 1]:
            case -= rcvCase[day - 1]

        print(day, case, newCase, rcvCase[day - 1])
        if rcvCase[day - 1]:
            immRate += rcvCase[day - 1] / ppl
            rcvCase[day - 1] = 0
        caseCount += newCase
        rcvCase[day + rcvDay - 1] += newCase
    print(caseCount)


if __name__ == "__main__":
    main()
