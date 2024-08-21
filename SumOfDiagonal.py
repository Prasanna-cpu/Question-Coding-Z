def diagonal_sum(matrix):
    main_sum=0
    secondary_sum=0

    n=len(matrix)

    for i in range(n):
        main_sum+=matrix[i][i]
        secondary_sum+=matrix[i][n-i-1]

    if n % 2 == 1:
        center_index = n // 2
        center_element = matrix[center_index][center_index]
        total_sum = main_sum + secondary_sum - center_element
    else:
        total_sum = main_sum + secondary_sum

    return total_sum