def equTri(n):
    j = 1
    for i in range(n - 1, -1, -1):
        print('#' * i, end='')
        print('*' * j, end='')
        j += 2
        print('#' * i)

def invTri(n):
    j = 2 * n - 1
    for i in range(n):
        print('#' * i, end='')
        print('*' * j, end='')
        j -= 2
        print('#' * i)

def rhombic(n):
    j = 1
    for i in range(n // 2, -1, -1):
        print(' ' * i, end='')
        print('*' * j)
        j += 2
    j = n - 2
    for i in range(1, n // 2 + 1, 1):
        print(' ' * i, end='')
        print('*' * j)
        j -= 2

def fishShape(n):
    j = 1
    k = n - 1
    l = 0
    for i in range(n // 2, -1, -1):
        print(' ' * i, end='')
        print('*' * j, end='')
        print(' ' * k, end='')
        print('-' * l)
        j += 2
        k -= 2
        l += 1
    j = n - 2
    k = 2
    l = n // 2 - 1
    for i in range(1, n // 2 + 1, 1):
        print(' ' * i, end='')
        print('*' * j, end='')
        print(' ' * k, end='')
        print('-' * l)
        j -= 2
        k += 2
        l -= 1

def main():
    c = int(input())
    n = int(input())
    if not 2 <= n <= 50 or n % 2 == 0:
        raise Exception
    if c == 1:
        equTri(n)
    elif c == 2:
        invTri(n)
    elif c == 3:
        rhombic(n)
    elif c == 4:
        fishShape(n)

if __name__ == '__main__':
    try:
        main()
    except Exception:
        print("error")
