def move_zeros(lst):
  result = []

  for x in lst:
    if x != 0:
      result.append(x)

  zero = [0] * lst.count(0)
  result.extend(zero)

  return result