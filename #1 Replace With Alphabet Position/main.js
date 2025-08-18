function alphabetPosition(text) {
  const arr = [];
  for (let i = 0; i < text.length; i++) {
    let char = text[i].toLowerCase();

    if (char >= "a" && char <= "z") {
      arr.push(char.charCodeAt(0) - 96);
    }
  }
  return arr.join(" ");
}

console.log(alphabetPosition("Hello world!"));
