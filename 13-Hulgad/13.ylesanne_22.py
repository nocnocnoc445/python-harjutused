koik_oskused = {"Python", "Git", "Linux", "SQL", "Docker"}
noutud_oskused = {"Python", "Git", "SQL"}

print("Olemasolevad oskused:", ", ".join(sorted(koik_oskused)))
print("Nõutud oskused:", ", ".join(sorted(noutud_oskused)))
print()

if noutud_oskused <= koik_oskused:
    print("Kõik nõutud oskused on olemas.")
else:
    puudu = noutud_oskused - koik_oskused
    print("Puuduvad oskused:", ", ".join(sorted(puudu)))

print("issubset() tulemus:", noutud_oskused.issubset(koik_oskused))
