# VIGA 1: muutuja nimes ei tohi olla tühikut ("student age") -> SyntaxError.
#         Parandus: kasuta alakriipsu: student_age
# VIGA 2: input() tagastab teksti, "17" + 1 annab TypeError.
#         Parandus: teisenda int() abil arvuks.
# (Lisaks: tulemust ei väljastatud, seega lisasin print().)

student_age = int(input("Vanus: "))
next_age = student_age + 1

print(next_age)