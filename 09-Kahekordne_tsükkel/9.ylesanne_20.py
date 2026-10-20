def keskmine(arvud):
    if len(arvud) == 0:
        return None
    return sum(arvud) / len(arvud)


print(keskmine([2, 4, 6, 8]))
print(keskmine([10, 20, 30]))
print(keskmine([]))