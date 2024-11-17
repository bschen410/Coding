def getTriangle(arr):
    if (arr[0] <= 0 or arr[1] <= 0 or arr[2] <= 0) or (arr[0] + arr[1] < arr[2]):
        print("not a triangle")
    elif arr[0] == arr[1] == arr[2]:
        print("equilateral triangle")
    elif arr[0] == arr[1] or arr[1] == arr[2]:
        print("isosceles triangle")
    elif arr[2] ** 2 > arr[0] ** 2 + arr[1] ** 2:
        print("obtuse triangle")
    elif arr[2] ** 2 < arr[0] ** 2 + arr[1] ** 2:
        print("acute triangle")
    elif arr[2] ** 2 == arr[0] ** 2 + arr[1] ** 2:
        print("right triangle")
arr = [int(input()), int(input()), int(input())]
arr.sort()
getTriangle(arr)
