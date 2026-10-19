from urllib.request import urlopen

URL = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"

with urlopen(URL) as vastus:
    tekst = vastus.read().decode("utf-8")

read = tekst.splitlines()
tuhjad = 0
for rida in read:
    if rida.strip() == "":
        tuhjad += 1

print("Veebiteksti statistika")
print("----------------------")
print("Ridu:", len(read))
print("Sõnu:", len(tekst.split()))
print("Tähemärke:", len(tekst))
print("Tühje ridu:", tuhjad)