def sort_array(source_array):
    odd = []
    for num in source_array:
        if num % 2 != 0:
            odd.append(num)

    odd.sort()
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odd.pop(0)
    return source_array

print(sort_array([5, 3, 2, 8, 1, 4]))
