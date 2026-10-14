# Ennustused:
# tahed[1:4]   -> ['B', 'C', 'D']
# tahed[:3]    -> ['A', 'B', 'C']
# tahed[3:]    -> ['D', 'E', 'F']
# tahed[-3:-1] -> ['D', 'E']
# tahed[::-1]  -> ['F', 'E', 'D', 'C', 'B', 'A']
#
# Selgitus: viilutamisel on lõpuindeks välja arvatud, et viilu pikkus
# oleks lihtsalt lõpp - algus (nt [1:4] annab 3 elementi) ja et
# järjestikused viilud nagu [:3] ja [3:] ei kattuks.

tahed = ["A", "B", "C", "D", "E", "F"]
print(tahed[1:4])
print(tahed[:3])
print(tahed[3:])
print(tahed[-3:-1])
print(tahed[::-1])