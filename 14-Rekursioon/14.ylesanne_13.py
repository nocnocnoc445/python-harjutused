def on_palindroom(tekst):
    tekst = tekst.lower()
    if len(tekst) <= 1:
        return True
    if tekst[0] != tekst[-1]:
        return False
    return on_palindroom(tekst[1:-1])


for sona in ["radar", "kook", "python", "Anna"]:
    print(f"on_palindroom({sona!r}) = {on_palindroom(sona)}")
