def on_paaris(arv):
    return arv % 2 == 0


assert on_paaris(4) is True
assert on_paaris(7) is False
assert on_paaris(-6) is True
assert on_paaris(-3) is False
assert on_paaris(0) is True

print("Kõik testid läbisid.")
