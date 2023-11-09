def almostquickSort(arr):
    p = arr[0]
    left = []
    equal = []
    right = []
    for i in arr:
        if i == p:
            equal.append(i)
        elif i < p:
            left.append(i)
        else:
            right.append(i)
    return left + equal + right


def quickSortRecursion(ar):
    p = ar[0]
    left = []
    equal = []
    right = []
    for i in ar:
        if i < p:
            left.append(i)
        elif i == p:
            equal.append(i)
        else:
            right.append(i)
    print(f"{left=}", f"{equal=}", f"{right=}")
    return (
        (quickSortRecursion(left) if len(set(left)) > 1 else left)
        + (quickSortRecursion(equal) if len(set(equal)) > 1 else equal)
        + (quickSortRecursion(right) if len(set(right)) > 1 else right)
    )


def quickSort(ar):
    p = ar[0]
    left = []
    equal = []
    right = []
    for i in ar:
        if i == p:
            equal.append(i)
        elif i < p:
            left.append(i)
        else:
            right.append(i)


def quickSort3(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        print(*less, *[pivot], *greater)
        return quickSort3(less) + [pivot] + quickSort3(greater)


print(quickSort3([5, 8, 1, 3, 7, 9, 2]))
