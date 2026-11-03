def keskmine_hinne(hinded):
    if not hinded:
        return None
    return sum(hinded.values()) / len(hinded)


hinded = {
    "Mari": 5,
    "Jüri": 3,
    "Kati": 4,
    "Andres": 5
}

print("Keskmine hinne:", keskmine_hinne(hinded))
print("Tühja sõnastiku keskmine:", keskmine_hinne({}))