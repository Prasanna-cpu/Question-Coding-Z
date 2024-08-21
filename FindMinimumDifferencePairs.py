def find_min_difference_pairs(arr):
    # Sort the array to easily find the minimum difference
    arr.sort()

    min_diff = float('inf')
    pairs = []

    # Find the minimum difference between adjacent elements
    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
            pairs = [(arr[i], arr[i + 1])]
        elif diff == min_diff:
            pairs.append((arr[i], arr[i + 1]))

    # Format the output to print the pairs
    result = []
    for pair in pairs:
        result.extend(pair)

    return result