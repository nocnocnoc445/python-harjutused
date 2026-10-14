# Ennustus:
# Funktsioonis: 20
# Põhiprogrammis: 100
#
# Funktsiooni sees olev arv = 20 loob uue lokaalse muutuja, millel on
# lihtsalt sama nimi. See ei muuda põhiprogrammi muutujat arv, nii et
# seal jääb väärtuseks 100.

arv = 100

def muuda():
    arv = 20
    print("Funktsioonis:", arv)

muuda()
print("Põhiprogrammis:", arv)