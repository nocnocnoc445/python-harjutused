from urllib.request import urlopen

URL = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"

with urlopen(URL) as vastus:
    tekst = vastus.read().decode("utf-8")

read = tekst.splitlines()

for nr, rida in enumerate(read[:10], start=1):
    print(f"{nr}: {rida}")