# Ennustus: funktsioon väljastab 25, aga print(tulemus) põhiprogrammis
# annab vea NameError.
#
# Põhjus: tulemus on lokaalne muutuja. See on olemas ainult funktsiooni
# sees ja kaob, kui funktsioon lõpetab.
#
# Parandus: funktsioon tagastab väärtuse return-iga ja põhiprogramm
# salvestab selle muutujasse.

def arvuta():
    tulemus = 25
    print(tulemus)
    return tulemus

tulemus = arvuta()
print(tulemus)