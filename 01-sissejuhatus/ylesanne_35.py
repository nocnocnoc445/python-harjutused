x = 5        # x = 5
y = x        # x = 5, y = 5 (y saab x-i väärtuse koopia)
x = 10       # x = 10, y = 5 (y ei muutu, sest ta ei ole x-iga seotud)
y = y + x    # x = 10, y = 5 + 10 = 15 (kasutab x-i UUT väärtust)

print(x)  # 10
print(y)  # 15