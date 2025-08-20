def expanded_form(num):
    str_num = str(num)
    arr = []
    ind = 0

    for i in str_num:
        if i != "0":
          arr.append(i+ ("0" * len(str_num[(ind+1):])))
        ind+=1

    return " + ".join(arr)
