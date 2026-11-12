failid = {
    "dokumendid": {
        "kool": {
            "ylesanne.py": None,
            "andmed.txt": None
        },
        "arved": {
            "arve.pdf": None
        }
    },
    "pildid": {
        "foto.jpg": None
    }
}


def otsi_fail(struktuur, failinimi, tee=""):
    for nimi, sisu in struktuur.items():
        uus_tee = nimi if tee == "" else f"{tee}/{nimi}"
        if sisu is None:
            if nimi == failinimi:
                return uus_tee
        else:
            leitud = otsi_fail(sisu, failinimi, uus_tee)
            if leitud is not None:
                return leitud
    return None


print("ylesanne.py ->", otsi_fail(failid, "ylesanne.py"))
print("arve.pdf ->", otsi_fail(failid, "arve.pdf"))
print("foto.jpg ->", otsi_fail(failid, "foto.jpg"))
print("puudub.txt ->", otsi_fail(failid, "puudub.txt"))

# sama failinime korral tagastatakse esimene leitud tee
korduv = {
    "a": {"memo.txt": None},
    "b": {"memo.txt": None}
}
print("memo.txt (kaks korda) ->", otsi_fail(korduv, "memo.txt"))

print()
nimi = input("Sisesta otsitava faili nimi: ").strip()
tee = otsi_fail(failid, nimi)
if tee is None:
    print("Faili ei leitud.")
else:
    print("Faili tee:", tee)
