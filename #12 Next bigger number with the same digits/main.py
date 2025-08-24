# TODO: bu kod bizga berilgan sonni raqamlar joyini almashtirib eng katta sonni topib beradi

def next_bigger(n):
    res = ''

    arr = [int(i) for i in str(n)]
    arr.sort(reverse=True)

    for i in range(len(arr)):
        res += str(arr[i])

    if int(res) == n:
        return -1
    else:
        return int(res)


# TODO:
def next_bigger1(n):
    digits = list(str(n))

    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i+1]:
        i-=1

    if i == -1:
        return -1

    j =len(digits) - 1
    while digits[j] <= digits[i]:
        j-=1

    digits[i], digits[j]= digits[j], digits[i]

    digits[i + 1 :] = sorted(digits[i + 1 :])

    return int("".join(digits))

print(next_bigger1(2017))