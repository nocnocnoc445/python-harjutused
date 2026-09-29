print(int("123"))       # 123
#int("12.3")            # ValueError
print(float("12.3"))    # 12.3
#float("tere")          # ValueError
print(str(25))          # 25

#int("12.3") ei tööta, sest int() ei loe teksti, milles on punkt. float("tere") ei tööta, sest „tere“ pole arv.