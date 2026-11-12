# käivitamine repo juurkaustast:
#   python3 -m pytest 15-Automaattestimine/15.ylesanne_26 -v

import sys
import pytest


def eemalda_kordused(andmed):
    nahtud = set()
    tulemus = []
    for element in andmed:
        if element not in nahtud:
            nahtud.add(element)
            tulemus.append(element)
    return tulemus


def test_tuhi_jarjend():
    assert eemalda_kordused([]) == []


def test_kordusteta_jarjend():
    assert eemalda_kordused([1, 2, 3]) == [1, 2, 3]


def test_ainult_kordused():
    assert eemalda_kordused([4, 4, 4, 4]) == [4]


def test_jarjekord_sailib():
    assert eemalda_kordused([3, 1, 3, 2, 1]) == [3, 1, 2]


def test_sonad():
    sonad = ["kass", "koer", "kass", "hiir", "koer"]
    assert eemalda_kordused(sonad) == ["kass", "koer", "hiir"]


def test_algne_jarjend_ei_muutu():
    andmed = [5, 5, 6, 7, 6]
    koopia = list(andmed)
    tulemus = eemalda_kordused(andmed)
    assert andmed == koopia
    assert tulemus is not andmed


if __name__ == "__main__":
    sys.exit(pytest.main(["-v", __file__]))
