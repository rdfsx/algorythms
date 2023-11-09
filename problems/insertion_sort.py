def insertionSort1(n, arr):
    val = arr[n - 1]

    for j in range(n - 1, -1, -1):
        if arr[j] > val:
            arr[j + 1] = arr[j]
            print(*arr)
            if j == 0:
                arr[j] = val
                print(*arr)
        elif arr[j] < val:
            arr[j + 1] = val
            print(*arr)
            break


def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                temp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = temp
        print(*arr)


insertionSort2(10, [1, 4, 3, 5, 6, 2])
