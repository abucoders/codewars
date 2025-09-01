def snail(array):
    result = []
    while array:
        # 1) Yuqori qatorni olamiz
        result += array.pop(0)

        # 2) Har bir qolgan qatordan oxirgi elementni olamiz
        if array and array[0]:
            for row in array:
                result.append(row.pop())

        # 3) Oxirgi qatorni teskari tartibda olamiz
        if array:
            result += array.pop()[::-1]

        # 4) Har bir qolgan qatordan birinchi elementni teskari tartibda olamiz
        if array and array[0]:
            for row in array[::-1]:
                result.append(row.pop(0))
    return result


print(snail([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]))
