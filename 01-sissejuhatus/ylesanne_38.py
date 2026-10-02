number = int(input("Sisesta arv: "))

a = number // 10   # täisarvuline jagamine: 47 // 10 = 4  -> kümnete number
b = number % 10    # jagamise jääk:          47 % 10  = 7  -> ühelised

print(a)
print(b)

# Testitud arvuga 47: väljund 4 ja 7.
# Programm jagab kahekohalise arvu numbriteks: a = kümnelised, b = ühelised.