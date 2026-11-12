# käivitamine:
#   cd 15-Automaattestimine/15.ylesanne_31
#   python3 -m unittest -v

import unittest


def liida(a, b):
    return a + b


class TestLiida(unittest.TestCase):

    def test_positiivsed(self):
        self.assertEqual(liida(2, 3), 5)

    def test_negatiivsed(self):
        self.assertEqual(liida(-4, -6), -10)

    def test_erimargilised(self):
        self.assertEqual(liida(-5, 8), 3)

    def test_nullid(self):
        self.assertEqual(liida(0, 0), 0)

    def test_suured_arvud(self):
        self.assertEqual(liida(1000000, 2500000), 3500000)

    def test_kumnendarvud(self):
        self.assertEqual(liida(1.5, 2.25), 3.75)


if __name__ == "__main__":
    unittest.main(verbosity=2)
