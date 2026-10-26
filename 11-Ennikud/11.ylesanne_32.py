def jaga_arvud(a, b):
    if b == 0:
        print(f"Arvu {a} ei saa jagada nulliga!")
        return None
    return a // b, a % b


for a, b in ((17, 5), (40, 8), (9, 0)):
    tulemus = jaga_arvud(a, b)
    if tulemus is not None:
        jagatis, jaak = tulemus
        print(f"{a} : {b} = {jagatis}, jääk {jaak}")
