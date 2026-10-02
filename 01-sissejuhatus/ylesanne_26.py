tunnid = int(input("Sisesta tundide arv: "))
päevad = tunnid // 24
ülejäänud_tunnid = tunnid % 24
print(päevad, "päeva ja", ülejäänud_tunnid, "tundi")