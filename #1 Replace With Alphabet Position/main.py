def alphabet_position(text):
    arr = []

    for i in text:
        if i.isalpha():
            arr.append(str(ord(i.lower()) - 96))

    return " ".join(arr)

print(alphabet_position("The sunset sets at twelve o' clock."))
