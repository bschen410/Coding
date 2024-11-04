def cal(name, h, w):
    h = int(h)
    w = int(w)
    emi = h * h % w
    if emi > 35:
        print("EMI too high")
        return [name, emi]
    elif emi < 10:
        print("EMI too low")
        return [name, emi]
    else:
        print(emi)
        return [name, emi]


def main():
    emi_list = list()
    while True:
        inp = input()
        if inp == "End":
            break
        data = inp.split()
        if not 50 <= int(data[1]) <= 250:
            print("Input Height Error")
        elif not 20 <= int(data[2]) <= 300:
            print("Input Weight Error")
        else:
            emi_list.append(cal(data[0], data[1], data[2]))
    sorted_emi_list = sorted(emi_list, key=lambda x: x[1], reverse=True)
    for i in range(len(sorted_emi_list)):
        print(sorted_emi_list[i][0], sorted_emi_list[i][1])
    print(emi_list)


main()
