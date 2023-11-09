def icecreamParlor(m, arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            if arr[i] + arr[j] == m:
                return [i + 1, j + 1]
