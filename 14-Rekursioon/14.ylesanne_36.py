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


def loenda_failid(struktuur):
    arv = 0
    for sisu in struktuur.values():
        if sisu is None:
            arv += 1
        else:
            arv += loenda_failid(sisu)
    return arv


print("Failide arv:", loenda_failid(kaustad))
