# käivitamine repo juurkaustast:
#   python3 -m pytest 15-Automaattestimine/15.ylesanne_35 -v

import sys
import pytest


# Red: testid kirjutati enne lahendust, funktsioonis oli ainult "pass".
#      Tulemus: 8 failed (funktsioon tagastas None).
# Green: esimene lahendus kontrollis kõiki jagajaid 2 kuni arv - 1.
#      Tulemus: 8 passed.
# Refactor: jagajaid piisab kontrollida kuni ruutjuureni, sest kui arvul
#      on jagaja, mis on suurem kui ruutjuur, on tal ka väiksem paariline.
#      Pärast muudatust läbivad testid jälle: 8 passed.

def on_algarv(arv):
    if arv < 2:
        return False
    jagaja = 2
    while jagaja * jagaja <= arv:
        if arv % jagaja == 0:
            return False
        jagaja += 1
    return True


@pytest.mark.parametrize("arv, oodatud", [
    (2, True),
    (3, True),
    (4, False),
    (9, False),
    (17, True),
    (1, False),
    (0, False),
    (-5, False),
])
def test_on_algarv(arv, oodatud):
    assert on_algarv(arv) == oodatud


if __name__ == "__main__":
    sys.exit(pytest.main(["-v", __file__]))
