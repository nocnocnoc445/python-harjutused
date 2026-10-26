seadmed = (
    ("Sülearvuti", 850, 5),
    ("Monitor", 220, 8),
    ("Klaviatuur", 45, 15),
    ("Hiir", 25, 20),
    ("Printer", 310, 3),
    ("Veebikaamera", 75, 6)
)

VAIKE_LAOSEIS = 7


def lao_vaartus(seadmed):
    summa = 0
    for nimetus, hind, kogus in seadmed:
        summa += hind * kogus
    return summa


def kalleim_seade(seadmed):
    kalleim_nimetus, kalleim_hind, kogus = seadmed[0]
    for nimetus, hind, kogus in seadmed:
        if hind > kalleim_hind:
            kalleim_nimetus = nimetus
            kalleim_hind = hind
    return kalleim_nimetus, kalleim_hind


def suurim_koguvaartus(seadmed):
    suurim_nimetus = ""
    suurim_vaartus = 0
    for nimetus, hind, kogus in seadmed:
        if hind * kogus > suurim_vaartus:
            suurim_nimetus = nimetus
            suurim_vaartus = hind * kogus
    return suurim_nimetus, suurim_vaartus


def vaikese_laoseisuga(seadmed, piir):
    leitud = []
    for nimetus, hind, kogus in seadmed:
        if kogus < piir:
            leitud.append((nimetus, kogus))
    return tuple(leitud)


def keskmine_uhikuhind(seadmed):
    summa = 0
    for nimetus, hind, kogus in seadmed:
        summa += hind
    return summa / len(seadmed)


def kuva_laoseis(seadmed):
    for nimetus, hind, kogus in seadmed:
        print(f"{nimetus}: {hind:.2f} € × {kogus} = {hind * kogus:.2f} €")


print("IT-SEADMETE LAOSEIS")
print()
kuva_laoseis(seadmed)

print()
print(f"Lao koguväärtus: {lao_vaartus(seadmed):.2f} €")

nimetus, hind = kalleim_seade(seadmed)
print()
print(f"Kõige kallim seade: {nimetus} ({hind:.2f} €)")

nimetus, vaartus = suurim_koguvaartus(seadmed)
print(f"Suurima koguväärtusega: {nimetus} ({vaartus:.2f} €)")

print()
print("Väikese laoseisuga seadmed:")
vaikesed = vaikese_laoseisuga(seadmed, VAIKE_LAOSEIS)
if len(vaikesed) == 0:
    print("- puuduvad")
for nimetus, kogus in vaikesed:
    print(f"- {nimetus} ({kogus} tk)")

print()
print(f"Keskmine ühikuhind: {keskmine_uhikuhind(seadmed):.2f} €")
