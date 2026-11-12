# käivitamine repo juurkaustast:
#   python3 -m pytest 15-Automaattestimine/15.ylesanne_40 -v

import sys
import pytest
from kalkulaator import liida, lahuta, korruta, jaga, astenda, jaak, arvuta


@pytest.mark.parametrize("a, b, oodatud", [
    (2, 3, 5),
    (-2, -3, -5),
    (0, 0, 0),
    (0.1, 0.2, 0.3),
])
def test_liida(a, b, oodatud):
    assert liida(a, b) == pytest.approx(oodatud)


@pytest.mark.parametrize("a, b, oodatud", [
    (10, 4, 6),
    (4, 10, -6),
    (-5, -5, 0),
    (2.5, 1.25, 1.25),
])
def test_lahuta(a, b, oodatud):
    assert lahuta(a, b) == pytest.approx(oodatud)


@pytest.mark.parametrize("a, b, oodatud", [
    (3, 4, 12),
    (-3, 4, -12),
    (-3, -4, 12),
    (5, 0, 0),
    (1.5, 2, 3),
])
def test_korruta(a, b, oodatud):
    assert korruta(a, b) == pytest.approx(oodatud)


@pytest.mark.parametrize("a, b, oodatud", [
    (10, 2, 5),
    (-9, 3, -3),
    (7, 2, 3.5),
    (0, 5, 0),
    (1, 3, 0.3333333),
])
def test_jaga(a, b, oodatud):
    assert jaga(a, b) == pytest.approx(oodatud)


@pytest.mark.parametrize("a, b, oodatud", [
    (2, 3, 8),
    (5, 0, 1),
    (2, -1, 0.5),
    (-2, 3, -8),
    (9, 0.5, 3),
])
def test_astenda(a, b, oodatud):
    assert astenda(a, b) == pytest.approx(oodatud)


@pytest.mark.parametrize("a, b, oodatud", [
    (10, 3, 1),
    (9, 3, 0),
    (-7, 3, 2),
    (7.5, 2, 1.5),
])
def test_jaak(a, b, oodatud):
    # Pythonis on jäägil sama märk mis jagajal, seega -7 % 3 annab 2
    assert jaak(a, b) == pytest.approx(oodatud)


def test_jaga_nulliga():
    with pytest.raises(ZeroDivisionError):
        jaga(5, 0)


def test_jaak_nulliga():
    with pytest.raises(ZeroDivisionError):
        jaak(5, 0)


@pytest.mark.parametrize("tehe, oodatud", [
    ("+", 14),
    ("-", 6),
    ("*", 40),
    ("/", 2.5),
    ("**", 10000),
    ("%", 2),
])
def test_arvuta_koik_tehted(tehe, oodatud):
    assert arvuta(10, 4, tehe) == pytest.approx(oodatud)


@pytest.mark.parametrize("tehe", ["x", "", "//", "plus"])
def test_arvuta_vigane_tehe(tehe):
    with pytest.raises(ValueError):
        arvuta(1, 2, tehe)


def test_arvuta_nulliga_jagamine():
    with pytest.raises(ZeroDivisionError):
        arvuta(8, 0, "/")


if __name__ == "__main__":
    sys.exit(pytest.main(["-v", __file__]))
