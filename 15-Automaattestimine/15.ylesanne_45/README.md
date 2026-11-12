# Ülesanne 45. Ostukorvi automaattestimine

## Failid

- `ostukorv.py` – ostukorvi funktsioonid
- `test_ostukorv.py` – pytest testid
- `README.md` – see fail

## Funktsioonid

| Funktsioon | Mida teeb |
|---|---|
| `arvuta_summa(ostukorv)` | tagastab toodete kogumaksumuse |
| `leia_kalleim(ostukorv)` | tagastab kõige kallima ühikuhinnaga toote nime |
| `toodete_arv(ostukorv)` | tagastab toodete koguse kokku |
| `rakenda_soodustus(summa, protsent)` | tagastab soodustusega summa |
| `eemalda_toode(ostukorv, nimi)` | tagastab uue ostukorvi ilma nimetatud tooteta |

## Testide käivitamine

Repo juurkaustast:

```
python3 -m pytest 15-Automaattestimine/15.ylesanne_45 -v
```

või selles kaustas:

```
python3 -m pytest -v
```

## Testimise tulemused

```
35 passed
```

Kokku on 35 testjuhtumit. Need kontrollivad kõiki viit funktsiooni,
tavalisi sisendeid, piirväärtusi (0% ja 100% soodustus, kogus 0, hind 0),
tühja ostukorvi, vigaseid väärtusi (negatiivne hind, negatiivne kogus,
kümnendarvuline kogus, tekstina antud hind) ja algandmete säilimist.
Testides on kasutatud `@pytest.mark.parametrize` dekoraatorit ja
`pytest.raises` konstruktsiooni. Iga test saab fixture'i kaudu oma
ostukorvi koopia, seega testid ei sõltu üksteisest.

## Testimisel avastatud probleem

Esimeses versioonis tagastas `arvuta_summa()` summa ümardamata ja test
võrdles seda täpselt arvuga 19.40. Test ebaõnnestus:

```
E       AssertionError: assert 19.400000000000002 == 19.4
```

Põhjus on ujukomaarvudes: näiteks `4.20 * 3` annab Pythonis
`12.600000000000001`, sest arvuti ei saa kõiki kümnendarve täpselt
salvestada. Lahendusena ümardab funktsioon rahasummad kahe kümnendkohani
(`round(summa, 2)`) ja testid võrdlevad tulemusi kahe kümnendkoha
täpsusega (`pytest.approx(..., abs=0.005)`).

Teine avastatud asi: Pythonis on `True` täisarvu alamtüüp, seega
`isinstance(True, int)` annab `True`. Ilma eraldi kontrollita oleks kogus
`True` läbinud kontrolli. Nüüd välistab `kontrolli_toodet()` tõeväärtused
eraldi ja selle kohta on oma test.
