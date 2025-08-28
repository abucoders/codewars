function solution(s) {
  let result = "";
  for (let i of s) {
    if (i === i.toUpperCase() && i !== i.toLowerCase()) {
      result += " " + i;
    } else {
      result += i;
    }
  }
  return result;
}
