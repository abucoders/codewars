# [Hashtag Generator]("https://www.codewars.com/kata/52449b062fb80683ec000024/train/javascript")

## 📌 Task
Given a string, generate a hashtag for marketing.

## ✅ Rules
1. The result **must start with** a hash sign: `#`.
2. **Capitalize** the **first letter of every word**; remove all spaces in the final result.
3. If the **final result** (including `#`) is **longer than 140 characters**, return `false`.
4. If the **input** is empty or only spaces, or if the processed result would be empty, return `false`.

---

## ✨ Examples
```text
" Hello there thanks for trying my Kata"  →  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  →  "#HelloWorld"
""                                        →  false
