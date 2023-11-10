def selection_sort(arr):
    print(arr)
    result = []
    while arr:
        min_ = arr[0]
        min_idx = 0
        for i in range(len(arr)):
            if arr[i] < min_:
                min_ = arr[i]
                min_idx = i
        result.append(min_)
        arr.pop(min_idx)
    return result


if __name__ == "__main__":
    print(
        selection_sort([3, 4, 5, 2, 4, 6, 3, 3, 55, 6, 2, 0, 4, 2, 1, 6, 5, 4, 200, 44, 44, 2, 4])
    )
