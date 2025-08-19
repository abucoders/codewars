# [Facebook-style "Likes" Display](https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/javascript)

## 📌 Task
Implement a function that takes an array of names (strings) — the people who “like” an item — and returns the display text according to the rules below.

## ✅ Rules
- If no one likes it: return **"no one likes this"**
- If exactly one person likes it: return **"{name} likes this"**
- If exactly two people like it: return **"{name1} and {name2} like this"**
- If exactly three people like it: return **"{name1}, {name2} and {name3} like this"**
- If four or more people like it: return **"{name1}, {name2} and {N} others like this"**,
  where **N = total_likes − 2**

> Note: For 4+ names, only the first two names are shown, and the rest are summarized as “N others”.

---

## 🧪 Examples
```text
[]                                --> "no one likes this"
["Peter"]                         --> "Peter likes this"
["Jacob", "Alex"]                 --> "Jacob and Alex like this"
["Max", "John", "Mark"]           --> "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  --> "Alex, Jacob and 2 others like this"
