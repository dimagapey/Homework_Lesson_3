# 1й способ:
some_n = int(input("Введите трехзначное число, пожалуйста: "))
d1 = some_n % 10
d2 = some_n % 100 // 10
d3 = some_n // 100
print("Сумма цифр введенного числа: ", d1 + d2 + d3)

# 2й способ:
any_number = input('Введите трехзначное число, пожалуйста: ')
any_n = 0
for i in any_number:
    any_n += int(i)
print(any_n)