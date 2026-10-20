tooted = ["Leib", "Piim", "Juust", "Õunad"]
muuk = [
    [12, 15, 10, 18, 20],
    [20, 18, 22, 19, 25],
    [8, 10, 7, 12, 9],
    [30, 25, 28, 35, 40]
]

print("TOODETE KOGUMÜÜK")
parim_toode = tooted[0]
parim_kogus = -1

for i in range(len(muuk)):
    kogus = 0
    for paev in muuk[i]:
        kogus += paev
    print(f"{tooted[i]:<8}{kogus}")
    if kogus > parim_kogus:
        parim_kogus = kogus
        parim_toode = tooted[i]

print()
print("PÄEVADE KOGUMÜÜK")
for paev in range(len(muuk[0])):
    kogus = 0
    for toode in range(len(muuk)):
        kogus += muuk[toode][paev]
    print(f"{paev + 1}. päev: {kogus}")

print()
print(f"Kõige rohkem müüdud toode: {parim_toode} ({parim_kogus} tk)")