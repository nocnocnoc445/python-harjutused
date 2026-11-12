tooted = {"leib", "piim", "juust", "või", "õun"}

print("Tooted:", ", ".join(sorted(tooted)))
toode = input("Millise toote soovid eemaldada? ").strip().lower()

if toode in tooted:
    tooted.remove(toode)
    print(f"Toode {toode} eemaldati.")
else:
    print(f"Toodet {toode} ei leitud.")

print("Alles jäänud tooted:", ", ".join(sorted(tooted)))
