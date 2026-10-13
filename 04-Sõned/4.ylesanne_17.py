sona = input("Sisesta sõna: ").lower()

if sona == sona[::-1]:
    print("Tegemist on palindroomiga.")
else:
    print("Tegemist ei ole palindroomiga.")