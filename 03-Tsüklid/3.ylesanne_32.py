from random import randint

salajane = randint(1, 10)

arvamus = int(input("Arva arv 1-10: "))

while arvamus != salajane:
    print("Vale!")
    print()
    arvamus = int(input("Arva arv 1-10: "))

print("Õige!")