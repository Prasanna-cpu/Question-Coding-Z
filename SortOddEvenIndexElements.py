def sort(arr):
    n = len(arr)
    odd_idx_elements = [arr[i] for i in range(n) if i % 2 == 0]
    even_idx_elements = [arr[i] for i in range(n) if i % 2 != 0]

    odd_idx_elements.sort(reverse=True)

    even_idx_elements.sort()

    result=[]
    odd_idx=0
    even_idx=0

    for i in range(n):
        if i % 2 == 0:
            result.append(odd_idx_elements[odd_idx])
            odd_idx += 1
        else:
            result.append(even_idx_elements[even_idx])
            even_idx += 1

    return result


print(sort([10, 3, 8, 7, 6, 4, 2, 5]))