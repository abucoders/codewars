function expandedForm(num) {
  str_num = String(num);
  arr = [];
  ind = 0;

  for (let i = 0; i < str_num.length; i++) {
    if (str_num[i] != 0) {
      arr.push(str_num[i] + "0".repeat(str_num.slice(ind + 1).length));
    }
    ind++;
  }
  return arr.join(" + ");
}
