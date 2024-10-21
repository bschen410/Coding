def rightTri(n):
    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end='')
        for j in range(i, 0, -1):
            print(j, end='')
        print()

def equTri(n):
    for i in range(n):
        print('_' * (n - i - 1), end='')
        for j in range(i + 1):
            print(j + 1, end='')
        for j in range(i, 0, -1):
            print(j, end='')
        print('_' * (n - i - 1), end='\n')

def invTri(n):
    for i in range(n - 1, -1, -1):
        print('_' * (n - i - 1), end='')
        for j in range(i + 1):
            print(j + 1, end='')
        for j in range(i, 0, -1):
            print(j, end='')
        print('_' * (n - i - 1), end='\n')

def main():
    m = int(input())
    n = int(input())
    if not 3 <= n <= 50 or not 1 <= m <= 3:
        raise Exception
    match m:
        case 1:
            rightTri(n)
        case 2:
            equTri(n)
        case 3:
            invTri(n)

if __name__ == '__main__':
    try:
        main()
    except Exception:
        print("error")
