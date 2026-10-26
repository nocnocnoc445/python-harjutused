def kalleim_toode(tooted):
    kalleim = tooted[0]
    for nimetus, hind in tooted:
        if hind > kalleim[1]:
            kalleim = (nimetus, hind)
    return kalleim


tooted = (
    ("Hiir", 25),
    ("Klaviatuur", 65),
    ("Monitor", 220),
    ("Veebikaamera", 89)
)

nimetus, hind = kalleim_toode(tooted)
print(f"Kõige kallim toode: {nimetus} ({hind} €)")
