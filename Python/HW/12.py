def cmp(a, b):
    total_a = 0
    for i in range(1, 4):
        total_a += trans(a[i])
    if (total_a > 10.5):
        total_a = 0
        print(f'{b[0]} Win')
    else:
        cmp2(a, b)

def cmp2(a, b):
    total_a = 0
    total_b = 0
    for i in range(1, 4):
        total_a += trans(a[i])
        total_b += trans(b[i])
    if (total_a > 10.5): total_a = 0
    if (total_b > 10.5): total_b = 0
    if (total_a > total_b):
        print(f'{a[0]} Win')
    elif (total_a < total_b):
        print(f'{b[0]} Win')
    else:
        print('Tie')

def trans(s):
    if s == 'A' or s == 'J' or s == 'Q' or s == 'K':
        return 0.5
    else:
        return int(s)

def main():
    player = [input() for _ in range(4)]
    banker = [input() for _ in range(4)]
    cmp(player, banker)
    cmp2(player, banker)

if __name__ == '__main__':
    main()
