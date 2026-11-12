# käivitamine repo juurkaustast:
#   python3 -m pytest 15-Automaattestimine/15.ylesanne_20 -v

import sys
import pytest


def kuup(arv):
    return arv ** 3


def test_kuup_kaks():
    assert kuup(2) == 8


def test_kuup_kolm():
    assert kuup(3) == 27


def test_kuup_negatiivne():
    assert kuup(-2) == -8


def test_kuup_null():
    assert kuup(0) == 0


def test_kuup_yks():
    assert kuup(1) == 1


# Esialgne funktsioon oli "return arv ** 2". pytest andis tulemuse
# "3 failed, 2 passed" ja näitas näiteks:
#   E       assert 4 == 8
#   E        +  where 4 = kuup(2)
# Vasakul on tegelik tulemus (4) ja paremal oodatud tulemus (8).
# Funktsioon arvutas ruudu, mitte kuubi. Testid kuup(0) ja kuup(1)
# läbisid ka vigase funktsiooniga, sest 0² = 0³ ja 1² = 1³, seega
# ainult nende kahe testiga poleks viga leitud.
# Parandus: ** 2 asemel ** 3. Pärast parandust läbivad kõik 5 testi.

if __name__ == "__main__":
    sys.exit(pytest.main(["-v", __file__]))
