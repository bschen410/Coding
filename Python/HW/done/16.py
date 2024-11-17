def getAreaOfTriangle(arr):
    s = sum(arr) / 2
    area = (s * (s - arr[0]) * (s - arr[1]) * (s - arr[2])) ** 0.5
    return area

def getTriangle(arr, count):
    area = getAreaOfTriangle(arr)
    #
    if (arr[0] <= 0 or arr[1] <= 0 or arr[2] <= 0) or (arr[0] + arr[1] <= arr[2]):
        print("not a triangle")
        count += 1
        return count, None
    elif arr[0] == arr[1] == arr[2]:
        print("equilateral triangle", '%.2f'%area)
    elif arr[0] == arr[1] or arr[1] == arr[2]:
        print("isosceles triangle", '%.2f'%area)
    elif arr[2] ** 2 > arr[0] ** 2 + arr[1] ** 2:
        print("obtuse triangle", '%.2f'%area)
    elif arr[2] ** 2 < arr[0] ** 2 + arr[1] ** 2:
        print("acute triangle", '%.2f'%area)
    elif arr[2] ** 2 == arr[0] ** 2 + arr[1] ** 2:
        print("right triangle", '%.2f'%area)
    #
    return count, area

def main():
    count = 0
    areas = list()
    n = int(input())
    for _ in range(n):
        arr = input().split()
        arr = [int(i) for i in arr]
        arr.sort()
        count, area = getTriangle(arr, count)
        areas.append(area)
    if count == n:
        print("All inputs are not triangles!")
    else:
        print('%.2f'%max([i for i in areas if i]))
        print('%.2f'%min([i for i in areas if i]))

if __name__ == '__main__':
    main()
