def rotate(arr, k, clockwise=True):
    n = len(arr)
    k = k % n
    if not clockwise:
        k = n - k
    return arr[-k:] + arr[:-k]
