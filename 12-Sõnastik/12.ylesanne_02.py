pealinnad = {
    "Eesti": "Tallinn",
    "Läti": "Riia",
    "Leedu": "Vilnius",
    "Soome": "Helsingi",
    "Rootsi": "Stockholm",
    "Norra": "Oslo",
    "Saksamaa": "Berliin"
}

riik = input("Sisesta riigi nimi: ").strip().capitalize()
print(f"{riik} pealinn on {pealinnad[riik]}.")