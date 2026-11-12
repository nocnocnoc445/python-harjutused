def tagurpidi(tekst):
    if tekst == "":
        return ""
    return tagurpidi(tekst[1:]) + tekst[0]


for sona in ["Python", "kala", ""]:
    print(f"tagurpidi({sona!r}) = {tagurpidi(sona)!r}")
