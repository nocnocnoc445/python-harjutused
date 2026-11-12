# käivitamine repo juurkaustast:
#   python3 -m pytest 15-Automaattestimine/15.ylesanne_36 -v

import sys
import pytest


# Red: 12 testi kirjutati enne lahendust, funktsioonis oli ainult "pass".
#      Tulemus: 12 failed.
# Green: esimene lahendus käis märgid tsükliga läbi ja pani kolm
#      tõeväärtust paika. Tulemus: 12 passed.
# Refactor: tsükkel asendati lühema any() kujuga. Testid läbivad jälle:
#      12 passed.

def parool_sobib(parool):
    if len(parool) < 8:
        return False
    on_suurtaht = any(mark.isupper() for mark in parool)
    on_vaiketaht = any(mark.islower() for mark in parool)
    on_number = any(mark.isdigit() for mark in parool)
    return on_suurtaht and on_vaiketaht and on_number


@pytest.mark.parametrize("parool, oodatud", [
    ("Parool12", True),
    ("Tere1234", True),
    ("Pa1bcdef", True),
    ("ÕunaPuu7", True),
    ("Pikk Parool 2026", True),
    ("Pa1bcde", False),
    ("Pa1", False),
    ("", False),
    ("parool123", False),
    ("PAROOL123", False),
    ("Paroolike", False),
    ("12345678", False),
])
def test_parool_sobib(parool, oodatud):
    assert parool_sobib(parool) == oodatud


if __name__ == "__main__":
    sys.exit(pytest.main(["-v", __file__]))
