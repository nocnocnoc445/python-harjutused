sekundid = int(input("Sisesta sekundid: "))
tunnid = sekundid // 3600
minutid = sekundid % 3600 // 60
ülejäänud_sekundid = sekundid % 60
print(sekundid, "sekundit =", tunnid, "h", minutid, "min", ülejäänud_sekundid, "s")