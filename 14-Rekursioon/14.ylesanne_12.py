TAISHAALIKUD = "aeiouõäöü"


def taishaalikud(tekst):
    if tekst == "":
        return 0
    if tekst[0].lower() in TAISHAALIKUD:
        return 1 + taishaalikud(tekst[1:])
    return taishaalikud(tekst[1:])


for tekst in ["Tere maailm", "Python", "xyz", "ÕUN"]:
    print(f"taishaalikud({tekst!r}) = {taishaalikud(tekst)}")
