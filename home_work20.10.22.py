# 30). Вычислить число π c заданной точностью d
# Пример:
# при d = 0.001,π = 3.141 10^(-1)≤d≤10^(-10)


# import math
# pi = math.pi
# d = str(input("Введите заданную точность: "))
# print(round(pi, len(d)-2))




# 31). Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 70 = 2*5*7 => [2, 5, 7] 
# 140 = 2*2*5*7 => [2, 2, 5, 7]
# 140|2
# 70|2
# 35|5
# 7|7


# def Factor(n):
#     numbers = []
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             numbers.append(d)
#             n //= d
#         else:
#             d += 1
#     if n > 1:
#         numbers.append(n)
#     return numbers
# n = int(input("Введите число для списка множетелей: "))
# print(Factor(n))


# 32). Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# в ручную заполняем список
# from unittest import result


# numbers = []
# for i in range(int(input("Введите длинну последовательности: "))):
#     numbers.append(int(input()))
# print(numbers)
# numbers2 = []
# for i in range(int(input("Введите длинну последовательности: "))):
#     numbers2.append(int(input()))
# print(numbers2)
# result = set(numbers) ^ set(numbers2)
# print(result)




# 33). Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать 
# в файл многочлен степени k и приравняйте его к нулю.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# 2*x*2 + 4*x + 5 = 0
# или
# 2*x^2 + 4*x + 5 = 0

# import random

# k = int(input("Введите степень для многочлена: "))
# numbers = []
# i = 0
# y = k
# while i < k + 1:
#     numbers1 = f'*x^{y}'
#     number2 = str(random.randint(0, 100))
#     number = number2 + numbers1
#     if number.startswith('0'):
#         number = ''
#     elif number.startswith('1'):
#         number = ''
#     else:
#         numbers.append(number)  
#     i += 1
#     y -= 1
# text = " + ".join(numbers).replace("x^1", 'x').replace('*x^0', '') + ' = 0' 
# print(text)
# my_file = open("задание33-уравнение1.txt", "w+")
# my_file.write(f"{str(text)}\n ")





# 34). Даны два файла, в каждом из которых находится запись многочлена, приравненного к нулю. Задача - сформировать файл, содержащий сумму
#  многочленов (суммируем подобные слагаемые).
# Пример:
# 1 Файл : 2*x2 + 4*x + 5 = 0
# 2 Файл : 4*x2 + 7*x + 9 = 0
# 3 Файл: (содержит результат) 6*x2 + 11*x + 14 = 0
# Пример:
# 1 Файл : 2*x3 + 4*x2 + 5*x + 1 = 0
# 2 Файл : 4*x2 + 7*x + 9 = 0
# 3 Файл: (содержит результат) 2*x3 + 8*x2 + 12

with open("задание33-уравнение1.txt") as f1:
    var1 = f1.readline()
    print(f'Многочлен первый:  {var1}')
with open("задание33-уравнение2.txt") as f2:
    var2 = f2.readline()
    print(f'Многочлен второй:  {var2}')
var1 = var1.split()[:-2]
var2 = var2.split()[:-2]
i = 0
i2 = 0
while i < len(var1):
    if var1[i] == '+':
        del var1[i]
    i += 1
print(f"Убарали лишние '+' и '= 0' из первого многочлена:  {var1}")
while i2 < len(var2):
    if var2[i2] == '+':
        del var2[i2]
    i2 += 1
print(f"Убарали лишние '+' и '= 0' из второго многочлена:  {var2}")

result1 = list (map (lambda x: int(x.split('*x')[0]), var1))
result2 = list (map (lambda x: int(x.split('*x')[0]), var2))
print(f'Выводим подобыне слагаемые:  {result1}')
print(f'Выводим подобыне слагаемые:  {result2}')
result = list (map (sum, zip (result1, result2)))
print(f'Результат сложения:  {result}')
i3 = 0
count = len(result)
result_end = []
while i3 < len(result):
    result_end.append(f"{result[i3]}*x^{count-1}")
    count -= 1
    i3 += 1
    if count == 2:
        result_end.append(f"{result[i3]}*x")
        result_end.append(str(result[-1]))
        break
print(f"Возвращаем переменные со степенями и получаем готовый многочлен: {' + '.join(result_end)} = 0")
