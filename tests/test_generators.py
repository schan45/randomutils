from randomutils.generators import (
    generate_password,
    random_word,
    random_matrix,
    random_dates,
    generate_pseudoword,
    random_float_list,
    shuffle_list,
    random_int_in_range,
    group_random_names
)

print("----- Tesztek: RandomUtils -----")

# 1. generate_password
print("\n[generate_password]")
print("12 karakteres jelszó:", generate_password(12))

# 2. random_word
print("\n[random_word]")
words = ["piros", "zöld", "kék"]
print("Lista:", words)
print("Véletlen szó:", random_word(words))

# 3. random_matrix
print("\n[random_matrix]")
matrix = random_matrix(3, 4, 0, 9)
print("3x4-es mátrix 0-9 között:")
for row in matrix:
    print(row)

# 4. random_dates
print("\n[random_dates]")
dates = random_dates("2022-01-01", "2022-01-10", 3)
print("3 véletlen dátum:", dates)

# 5. generate_pseudoword
print("\n[generate_pseudoword]")
print("Példaszó:", generate_pseudoword(6))

# 6. random_float_list
print("\n[random_float_list]")
floats = random_float_list(5, 1.0, 2.0)
print("5 float 1.0 és 2.0 között:", floats)

# 7. shuffle_list
print("\n[shuffle_list]")
original = [1, 2, 3, 4, 5]
shuffled = shuffle_list(original)
print("Eredeti lista:", original)
print("Megkevert lista:", shuffled)

# 8. random_int_in_range
print("\n[random_int_in_range]")
print("Szám 10 és 20 között:", random_int_in_range(10, 20))

# 9. group_random_names
print("\n[group_random_names]")
names = ["Anna", "Béla", "Csaba", "Dóra", "Erik", "Fruzsi", "Gábor"]
groups = group_random_names(names, 3)

for i, g in enumerate(groups, start=1):
    print(f"{i}. csoport: {g}")


print("\n✅ Minden funkció sikeresen futott!")
