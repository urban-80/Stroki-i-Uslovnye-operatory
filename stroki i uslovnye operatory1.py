try:
    chislo1 = int(input("Введите число: "))
except ValueError:
    print("Вы ввели не число")
if  100 < chislo1 < 1000:
    sum = int(str(chislo1)[0]) * int(str(chislo1)[1]) * int(str(chislo1)[2])
    print(sum)
else:
    print("Число не трехзначное")

try:
    chislo1 = int(input("Введите число: "))
except ValueError:
    print("Вы ввели не число")
if 100 < chislo1 < 1000:
    sum = int(str(chislo1)[0]) * int(str(chislo1)[1]) * int(str(chislo1)[2])
    print(sum)
else:
    print("Число не трехзначное")