sonad = ["arvuti", "programmeerimine", "hiir", "klaviatuur", "monitor"]

pikim = sonad[0]
luhim = sonad[0]

for sona in sonad:
    if len(sona) > len(pikim):
        pikim = sona
    if len(sona) < len(luhim):
        luhim = sona

print(f"Kõige pikem sõna: {pikim} ({len(pikim)} tähte)")
print(f"Kõige lühem sõna: {luhim} ({len(luhim)} tähte)")