# käivitamine repo juurkaustast:
#   python3 -m pytest 15-Automaattestimine/15.ylesanne_19 -v

import sys
import pytest
from calculator import liida, lahuta, korruta, jaga


def test_liida_positiivsed():
    assert liida(2, 3) == 5


def test_liida_negatiivsed():
    assert liida(-2, -3) == -5


def test_liida_kumnendarvud():
    assert liida(0.1, 0.2) == pytest.approx(0.3)


def test_lahuta_positiivsed():
    assert lahuta(10, 4) == 6


def test_lahuta_tulemus_negatiivne():
    assert lahuta(4, 10) == -6


def test_lahuta_null():
    assert lahuta(7, 0) == 7


def test_korruta_positiivsed():
    assert korruta(3, 4) == 12


def test_korruta_negatiivsega():
    assert korruta(-3, 4) == -12


def test_korruta_nulliga():
    assert korruta(5, 0) == 0


def test_jaga_taisarvuline_tulemus():
    assert jaga(10, 2) == 5


def test_jaga_kumnendtulemus():
    assert jaga(7, 2) == 3.5


def test_jaga_negatiivsed():
    assert jaga(-9, 3) == -3


def test_jaga_nulliga():
    with pytest.raises(ZeroDivisionError):
        jaga(5, 0)


if __name__ == "__main__":
    sys.exit(pytest.main(["-v", __file__]))
