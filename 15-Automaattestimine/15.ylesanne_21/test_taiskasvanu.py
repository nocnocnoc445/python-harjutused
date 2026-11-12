# käivitamine repo juurkaustast:
#   python3 -m pytest 15-Automaattestimine/15.ylesanne_21 -v

import sys
import pytest


def on_taiskasvanu(vanus):
    return vanus >= 18


@pytest.mark.parametrize("vanus, oodatud", [
    (0, False),
    (5, False),
    (16, False),
    (17, False),
    (18, True),
    (19, True),
    (30, True),
    (65, True),
    (100, True),
])
def test_on_taiskasvanu(vanus, oodatud):
    assert on_taiskasvanu(vanus) == oodatud


if __name__ == "__main__":
    sys.exit(pytest.main(["-v", __file__]))
