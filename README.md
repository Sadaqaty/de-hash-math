# 🔐 Expression Hash Cracker

A lightweight and universal Python script to **reverse-engineer hashed mathematical or alphanumeric expressions**.  

This script is especially useful when the original hash was generated from simple expressions like `2+2`, `a1*b3`, `3/1+2`, etc. It attempts to **brute-force** the original expression by trying every possible combination of characters and math operators, comparing the hash of each to the given hash.

---

## 💡 Use Case

While analyzing browser data or captured input fields, you might stumble upon a **hashed value** representing simple expressions. For example, maybe the user typed `3+3`, and it was stored as a hash.

As a beginner, you may not know what that hash represents. This script helps you **"de-hash"** that value by brute-forcing a list of plausible expressions.

---

## 🚀 Features

- 🔁 Brute-force all combinations of digits, letters, and operators
- 🔒 Supports multiple hash algorithms: `sha256`, `sha3_256`, `blake2s`, `ripemd256`
- 📏 Configurable expression length
- 🔍 Smart logging to track progress
- 🧠 Auto-attempts all listed hash types

---

## 📦 Requirements

- Python 3.x  
- Standard libraries: `argparse`, `itertools`, `hashlib`, `string`, `logging`

No external libraries required.

---

## ⚙️ Usage

```bash
python3 crack_expr_hash.py --hash <HASH_TO_CRACK> --ops "+-*/" --maxlen 5
```
### 🔸 Parameters

| Argument   | Description                                     | Example     |
|------------|-------------------------------------------------|-------------|
| `--hash`   | The target hash you want to crack               | `e4b93...`  |
| `--ops`    | Operators to include in expression attempts     | `+-*/`      |
| `--maxlen` | Maximum length of expressions to test           | `5 (default)` |

## 🧪 Example

```bash
python3 crack_expr_hash.py --hash 1a79a4d60de6718e8e5b326e338ae533 --ops "+" --maxlen 3
```
