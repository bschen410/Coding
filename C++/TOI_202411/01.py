a = list()
b = list()


def cal(l):
    if l[0] % 3 == 0:
        output = max(l)
        print(max(l))
        for i in range(5):
            if l[i] == max(l):
                l[i] //= 2
        return output
    else:
        output = min([i for i in l if i != 0])
        print(output)
        l = [i - 1 if i == output else i for i in l]
        return output


def main():
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    output = 1
    while output:
        if output % 2:
            output = cal(a)
        else:
            output = cal(b)


main()
