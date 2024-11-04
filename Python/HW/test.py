def convert(s):
    table = ["A"] + [str(i) for i in range(2, 11)]
    if s in table:
        print(table.index(s))
    elif s in ["J", "Q", "K"]:
        return 0.5


print(convert("5"))
