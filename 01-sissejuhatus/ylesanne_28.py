a = 20
b = a        # b saab a väärtuse koopia (20), mitte viite muutujale a
a = 35       # a muutub 35-ks, b jääb endiselt 20
b = b + 5    # b = 20 + 5 = 25

print(a)  # 35
print(b)  # 25

# Põhjendus:
# Rida "b = a" kopeerib a tolle hetke väärtuse (20) muutujasse b.
# Hilisem a muutmine (a = 35) b-d ei mõjuta, sest b ei ole a-ga seotud.
# Seejärel b = 20 + 5 = 25. Seega lõpus a = 35 ja b = 25.