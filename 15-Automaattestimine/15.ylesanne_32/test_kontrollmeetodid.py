# käivitamine:
#   cd 15-Automaattestimine/15.ylesanne_32
#   python3 -m unittest -v

import unittest


def on_paaris(arv):
    return arv % 2 == 0


def loe_tahed(tekst):
    arv = 0
    for mark in tekst:
        if mark.isalpha():
            arv += 1
    return arv


def leia_element(andmed, element):
    return element in andmed


class TestOnPaaris(unittest.TestCase):

    def test_paarisarv(self):
        self.assertTrue(on_paaris(4))

    def test_paaritu_arv(self):
        self.assertFalse(on_paaris(7))

    def test_null(self):
        self.assertTrue(on_paaris(0))

    def test_negatiivne_paaritu(self):
        self.assertFalse(on_paaris(-3))


class TestLoeTahed(unittest.TestCase):

    def test_tahed_ja_numbrid(self):
        self.assertEqual(loe_tahed("Tere123"), 4)

    def test_tuhi_sone(self):
        self.assertEqual(loe_tahed(""), 0)

    def test_eesti_tahed_ja_tuhikud(self):
        self.assertEqual(loe_tahed("öö ja päev"), 8)


class TestLeiaElement(unittest.TestCase):

    def setUp(self):
        self.nimed = ["Mari", "Jüri", "Kati"]

    def test_olemasolev_element(self):
        self.assertTrue(leia_element(self.nimed, "Jüri"))
        self.assertIn("Jüri", self.nimed)

    def test_puuduv_element(self):
        self.assertFalse(leia_element(self.nimed, "Peeter"))
        self.assertNotIn("Peeter", self.nimed)

    def test_tuhi_jarjend(self):
        self.assertFalse(leia_element([], "Mari"))

    def test_tagastab_toevaartuse(self):
        self.assertIn(leia_element(self.nimed, "Mari"), (True, False))


if __name__ == "__main__":
    unittest.main(verbosity=2)
