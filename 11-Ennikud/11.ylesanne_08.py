arvud = (3, 6, 9, 12, 15, 18, 21, 24, 27, 30)

print("Esimesed neli elementi:", arvud[:4])
print("Viimased kolm elementi:", arvud[-3:])
# viilu lõpuindeks ise ei kuulu tulemusse, seega indeksite 2-6 jaoks on lõpp 7
print("Elemendid indeksitega 2-6:", arvud[2:7])
print("Iga teine element:", arvud[::2])
