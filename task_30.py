# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность 
# и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Ввод: 7 2 5  Вывод: 7 9 11 13 15

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
res = []
n = a + (c - 1) * b + 1
for a in range(a, n, b):
    res.append(a)
print(res)
