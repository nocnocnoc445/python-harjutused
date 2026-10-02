minutid = int(input("Sisesta minutid: "))
tunnid = minutid // 60
ülejäänud_minutid = minutid % 60
print(tunnid, "tundi ja", ülejäänud_minutid, "minutit")