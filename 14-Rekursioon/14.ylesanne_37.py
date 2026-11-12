kaustad = {
    "projekt": {
        "src": {
            "main.py": None,
            "utils.py": None
        },
        "tests": {
            "test_main.py": None
        },
        "README.md": None
    }
}


def failiteed(struktuur, tee=""):
    teed = []
    for nimi, sisu in struktuur.items():
        uus_tee = nimi if tee == "" else f"{tee}/{nimi}"
        if sisu is None:
            teed.append(uus_tee)
        else:
            teed.extend(failiteed(sisu, uus_tee))
    return teed


for tee in failiteed(kaustad):
    print(tee)

# test sügavama struktuuriga
sugav = {"a": {"b": {"c": {"d": {"fail.txt": None}}}}, "juur.txt": None}
print()
print(failiteed(sugav))
