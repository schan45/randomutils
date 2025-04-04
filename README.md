# 🎲 randomutils

Ez a projekt egy egyszerű, saját készítésű Python csomag, amely különféle véletlenszerű értékeket tud generálni, például jelszavakat, karakterláncokat, mátrixokat, dátumokat, neveket és pszeudoszavakat.

---

## 📦 Telepítés

Fejlesztői módban:

```bash
pip install -e .
```

Ez lehetővé teszi a csomag szerkesztés közbeni azonnali használatát.

---

## 🧪 Tesztelés

Egyszerű tesztfájl, amely terminálban futtatható:

```bash
python tests/test_generators.py
```

---

## 📁 Fő funkciók

| Funkció | Leírás |
|--------|--------|
| `generate_password(length=12)` | Véletlen jelszó generálása |
| `random_word(words)` | Véletlen szó egy listából |
| `random_matrix(rows, cols, min, max)` | Mátrix generálása egész számokkal |
| `random_dates(start, end, count)` | Véletlen dátumok adott intervallumból |
| `random_string(length, ...)` | Alfanumerikus string több opcióval |
| `shuffle_list(list)` | Lista elemeinek megkeverése |
| `random_int_in_range(start, end)` | Egész szám generálása adott intervallumból |
| `random_name(names)` | Véletlen név kiválasztása |
| `group_random_names(names, groups)` | Névlista szétosztása véletlenszerű csoportokra |
| `generate_pseudoword(length)` | „Értelmesnek tűnő” pszeudoszó generálása |

---

## 📒 Példanotebook

A `randomutils_demo.ipynb` fájlban (az `examples/` mappában) bemutatjuk az összes funkció használatát interaktívan, Google Colab-kompatibilisen.

---

## 📚 Dokumentáció

A projekt teljes dokumentációja elérhető itt:  
🔗 [https://randomutils.readthedocs.io/en/latest/](https://randomutils.readthedocs.io/en/latest/)

---

## 📋 Függőségek

Lásd: `requirements.txt`

---

Készítette: Schleier Anna  
Licenc: MIT
