# Ennustus:
# Algus
# C
# A
# B
# D
# Lõpp
#
# teine() väljastab kõigepealt C, siis kutsub esimene(), mis väljastab
# A ja B, ning pärast seda jätkab teine() ja väljastab D.

def esimene():
    print("A")
    print("B")

def teine():
    print("C")
    esimene()
    print("D")

print("Algus")
teine()
print("Lõpp")