from random import randint

salajane = randint(1, 100)

arvamus = int(input("Arva arv 1-100: "))

while arvamus != salajane:
    if arvamus < salajane:
        print("Salajane arv on suurem.")
    else:
        print("Salajane arv on väiksem.")
    print()
    arvamus = int(input("Arva arv 1-100: "))

print("Õige!")