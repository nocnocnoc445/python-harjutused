sonad = ["Python", "programmeerimine", "järjend", "tsükkel", "fail"]

for sona in sonad:
    print(f"{sona} - {len(sona)} tähemärki")

print()

for sona in sonad:
    print(f"{sona}: esimene täht {sona[0]}, viimane täht {sona[-1]}")