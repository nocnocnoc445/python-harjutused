sonad = ("kass", "arvuti", "maja", "programm", "puu", "klaviatuur", "auto")

sobivaid = 0
for sona in sonad:
    if len(sona) >= 5:
        print(sona)
        sobivaid += 1

print("Vähemalt viietäheliste sõnade arv:", sobivaid)
