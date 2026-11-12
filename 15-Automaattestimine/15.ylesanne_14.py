def eemalda_tahed(tekst):
    tulemus = ""
    for mark in tekst:
        if not mark.isalpha():
            tulemus += mark
    return tulemus


assert eemalda_tahed("ab12c") == "12"
assert eemalda_tahed("123") == "123"
assert eemalda_tahed("abc") == ""
assert eemalda_tahed("a!2?") == "!2?"
assert eemalda_tahed("") == ""

print("Kõik testid läbisid.")
