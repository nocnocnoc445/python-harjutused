import math


def celsius_fahrenheit(c):
    return c * 9 / 5 + 32


# kümnendarvude puhul võrreldakse ligikaudselt, sest ujukomaarvud
# ei ole alati täpsed (näiteks 37 °C annab 98.60000000000001)
assert math.isclose(celsius_fahrenheit(0), 32)
assert math.isclose(celsius_fahrenheit(100), 212)
assert math.isclose(celsius_fahrenheit(-40), -40)
assert math.isclose(celsius_fahrenheit(37), 98.6)
assert math.isclose(celsius_fahrenheit(36.6), 97.88)
assert math.isclose(celsius_fahrenheit(-17.5), 0.5)

print("Kõik testid läbisid.")
