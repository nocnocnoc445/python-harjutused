# käivitamine repo juurkaustast:
#   python3 -m pytest 15-Automaattestimine/15.ylesanne_25 -v

import sys
import pytest


def leia_suurim(arvud):
    if not arvud:
        raise ValueError("Tühjal järjendil pole suurimat väärtust.")
    suurim = arvud[0]
    for arv in arvud[1:]:
        if arv > suurim:
            suurim = arv
    return suurim


def test_tavaline_jarjend():
    assert leia_suurim([3, 8, 1]) == 8


def test_uks_element():
    assert leia_suurim([5]) == 5


def test_negatiivsed_arvud():
    assert leia_suurim([-4, -1, -9]) == -1


def test_koik_vordsed():
    assert leia_suurim([7, 7, 7]) == 7


def test_korduv_suurim():
    assert leia_suurim([2, 9, 9, 1]) == 9


def test_suurim_alguses_ja_lopus():
    assert leia_suurim([10, 3, 4]) == 10
    assert leia_suurim([3, 4, 10]) == 10


def test_kumnendarvud():
    assert leia_suurim([1.5, 2.75, 0.5]) == 2.75


def test_tuhi_jarjend():
    with pytest.raises(ValueError):
        leia_suurim([])


if __name__ == "__main__":
    sys.exit(pytest.main(["-v", __file__]))
