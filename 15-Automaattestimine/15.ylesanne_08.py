def maarake_hinne(punktid):
    if punktid < 0 or punktid > 100:
        raise ValueError("Punktid peavad olema vahemikus 0–100.")
    if punktid >= 90:
        return 5
    if punktid >= 75:
        return 4
    if punktid >= 50:
        return 3
    if punktid >= 20:
        return 2
    return 1


def tekitab_vaartusvea(punktid):
    try:
        maarake_hinne(punktid)
    except ValueError:
        return True
    return False


assert maarake_hinne(0) == 1
assert maarake_hinne(19) == 1
assert maarake_hinne(20) == 2
assert maarake_hinne(49) == 2
assert maarake_hinne(50) == 3
assert maarake_hinne(74) == 3
assert maarake_hinne(75) == 4
assert maarake_hinne(89) == 4
assert maarake_hinne(90) == 5
assert maarake_hinne(100) == 5
assert tekitab_vaartusvea(-1)
assert tekitab_vaartusvea(101)

print("Kõik testid läbisid.")
