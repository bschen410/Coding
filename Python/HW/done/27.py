def chk(d):
    string = input()
    res = ""
    seq = list()
    left = ["(", "[", "{"]
    right = [")", "]", "}"]
    for s in string:
        if s in left:
            seq.append(s)
        elif s in right:
            tmp = seq.pop()
            if not tmp == left[right.index(s)]:
                raise Exception
        elif len(seq) == d:
            res += s
    if len(seq):
        raise Exception
    return res


def main():
    n = int(input())
    d = int(input())
    for _ in range(n):
        try:
            output = chk(d)
            # print(f"pass, {"EMPTY" if output == "" else output}")
            if output == "":
                print("pass, EMPTY")
            else:
                print("pass,", output)
        except:
            print("fail")


if __name__ == "__main__":
    main()
