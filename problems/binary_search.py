def binary_search(arr, element):
    new_arr = arr
    while True:
        idx = len(new_arr) // 2
        mid = new_arr[idx]
        if element == mid:
            return mid
        if element < mid:
            new_arr = new_arr[:idx]
        elif element > mid:
            new_arr = new_arr[idx:]
        else:
            break
    return False


if __name__ == "__main__":
    print(binary_search([x for x in range(1973)], 666))
