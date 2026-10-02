ÜHIKUD = {"cm": 0.00001, "m": 0.001, "km": 1}

km = float(input("Sisesta km: "))
meetrid = km / ÜHIKUD["m"]
sentimeetrid = km / ÜHIKUD["cm"]

print(f"{km:.10g} km = {meetrid:.10g} m")
print(f"{km:.10g} km = {sentimeetrid:.10g} cm")