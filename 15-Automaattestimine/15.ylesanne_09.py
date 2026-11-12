def on_palindroom(tekst):
    puhas = tekst.replace(" ", "").lower()
    return puhas == puhas[::-1]


assert on_palindroom("anna") is True
assert on_palindroom("kajak") is True
assert on_palindroom("") is True
assert on_palindroom("Aias sadas saia") is True
assert on_palindroom("Kirik") is True
assert on_palindroom("a") is True
assert on_palindroom("python") is False
assert on_palindroom("tere") is False

print("Kõik testid läbisid.")
