def loenda_alla(n):
    if n == 0:
        print(0)
        return
    print(n)
    loenda_alla(n - 1)


loenda_alla(5)
