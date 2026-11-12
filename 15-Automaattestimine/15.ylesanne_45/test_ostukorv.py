import copy
import sys
import pytest
from ostukorv import (
    arvuta_summa,
    leia_kalleim,
    toodete_arv,
    rakenda_soodustus,
    eemalda_toode,
)


# iga test saab oma uue koopia, seega testid ei sõltu üksteisest
@pytest.fixture
def ostukorv():
    return {
        "Leib": {"hind": 2.50, "kogus": 2},
        "Piim": {"hind": 1.80, "kogus": 1},
        "Juust": {"hind": 4.20, "kogus": 3},
    }


# arvuta_summa

def test_summa_naidisandmed(ostukorv):
    assert arvuta_summa(ostukorv) == pytest.approx(19.40, abs=0.005)


def test_summa_tuhi_ostukorv():
    assert arvuta_summa({}) == 0


def test_summa_uks_toode():
    assert arvuta_summa({"Leib": {"hind": 2.50, "kogus": 2}}) == pytest.approx(5.00, abs=0.005)


def test_summa_kogus_null():
    assert arvuta_summa({"Piim": {"hind": 1.80, "kogus": 0}}) == 0


def test_summa_hind_null():
    assert arvuta_summa({"Kingitus": {"hind": 0, "kogus": 5}}) == 0


def test_summa_kumnendarvud():
    assert arvuta_summa({"Kumm": {"hind": 0.10, "kogus": 3}}) == pytest.approx(0.30, abs=0.005)


def test_summa_ei_muuda_ostukorvi(ostukorv):
    algne = copy.deepcopy(ostukorv)
    arvuta_summa(ostukorv)
    assert ostukorv == algne


@pytest.mark.parametrize("vigane_toode", [
    {"hind": -1.00, "kogus": 1},
    {"hind": 2.00, "kogus": -1},
    {"hind": 2.00, "kogus": 1.5},
    {"hind": "2.00", "kogus": 1},
    {"hind": 2.00, "kogus": True},
])
def test_vigased_andmed_tekitavad_vea(vigane_toode):
    with pytest.raises(ValueError):
        arvuta_summa({"Toode": vigane_toode})


# leia_kalleim

def test_kalleim_naidisandmed(ostukorv):
    assert leia_kalleim(ostukorv) == "Juust"


def test_kalleim_tuhi_ostukorv():
    assert leia_kalleim({}) is None


def test_kalleim_uks_toode():
    assert leia_kalleim({"Piim": {"hind": 1.80, "kogus": 1}}) == "Piim"


def test_kalleim_vordne_hind_tahestik():
    ostukorv = {
        "Banaan": {"hind": 3.00, "kogus": 1},
        "Apelsin": {"hind": 3.00, "kogus": 2},
        "Õun": {"hind": 1.00, "kogus": 4},
    }
    assert leia_kalleim(ostukorv) == "Apelsin"


def test_kalleim_negatiivne_hind():
    with pytest.raises(ValueError):
        leia_kalleim({"Toode": {"hind": -5, "kogus": 1}})


# toodete_arv

def test_toodete_arv_naidisandmed(ostukorv):
    assert toodete_arv(ostukorv) == 6


def test_toodete_arv_tuhi_ostukorv():
    assert toodete_arv({}) == 0


def test_toodete_arv_kogus_null():
    ostukorv = {
        "Leib": {"hind": 2.50, "kogus": 0},
        "Piim": {"hind": 1.80, "kogus": 2},
    }
    assert toodete_arv(ostukorv) == 2


# rakenda_soodustus

@pytest.mark.parametrize("summa, protsent, oodatud", [
    (100, 0, 100),
    (100, 100, 0),
    (100, 25, 75),
    (19.40, 10, 17.46),
    (50, 12.5, 43.75),
])
def test_soodustus(summa, protsent, oodatud):
    assert rakenda_soodustus(summa, protsent) == pytest.approx(oodatud, abs=0.005)


@pytest.mark.parametrize("protsent", [-1, -0.5, 100.5, 101])
def test_soodustus_vigane_protsent(protsent):
    with pytest.raises(ValueError):
        rakenda_soodustus(100, protsent)


def test_soodustus_negatiivne_summa():
    with pytest.raises(ValueError):
        rakenda_soodustus(-10, 10)


# eemalda_toode

def test_eemalda_olemasolev_toode(ostukorv):
    uus = eemalda_toode(ostukorv, "Piim")
    assert "Piim" not in uus
    assert sorted(uus) == ["Juust", "Leib"]


def test_eemalda_ei_muuda_algset(ostukorv):
    algne = copy.deepcopy(ostukorv)
    eemalda_toode(ostukorv, "Leib")
    assert ostukorv == algne


def test_eemalda_puuduv_toode(ostukorv):
    uus = eemalda_toode(ostukorv, "Kohv")
    assert uus == ostukorv
    assert uus is not ostukorv


def test_eemalda_tuhjast_ostukorvist():
    assert eemalda_toode({}, "Leib") == {}


def test_eemalda_uus_korv_on_eraldi(ostukorv):
    uus = eemalda_toode(ostukorv, "Piim")
    uus["Leib"]["kogus"] = 99
    assert ostukorv["Leib"]["kogus"] == 2


if __name__ == "__main__":
    sys.exit(pytest.main(["-v", __file__]))
