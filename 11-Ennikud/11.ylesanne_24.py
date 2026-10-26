toode = ("Monitor", 199.99, 5)

nimetus, hind, kogus = toode
maksumus = hind * kogus

print("OSTU KOKKUVÕTE")
print("Toode:", nimetus)
print(f"Ühikuhind: {hind:.2f} €")
print(f"Kogus: {kogus} tk")
print(f"Kogumaksumus: {maksumus:.2f} €")
