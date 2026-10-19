from urllib.request import urlopen

URL = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"

# with sulgeb ühenduse automaatselt
with urlopen(URL) as vastus:
    baidid = vastus.read()

tekst = baidid.decode("utf-8")
print(tekst)