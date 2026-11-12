# käivitamine repo juurkaustast:
#   python3 -m pytest 15-Automaattestimine/15.ylesanne_22 -v

import math
import sys
import pytest


def ruutjuur(arv):
    if arv < 0:
        raise ValueError("Negatiivse arvu ruutjuurt ei saa leida.")
    return math.sqrt(arv)


@pytest.mark.parametrize("arv, oodatud", [
    (0, 0),
    (1, 1),
    (16, 4),
    (0.25, 0.5),
    (2, 1.41421356),
])
def test_ruutjuur(arv, oodatud):
    assert ruutjuur(arv) == pytest.approx(oodatud)


def test_ruutjuur_negatiivne_taisarv():
    with pytest.raises(ValueError):
        ruutjuur(-1)


def test_ruutjuur_negatiivne_kumnendarv():
    with pytest.raises(ValueError, match="Negatiivse"):
        ruutjuur(-0.5)


if __name__ == "__main__":
    sys.exit(pytest.main(["-v", __file__]))
