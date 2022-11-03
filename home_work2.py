# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 0,56 -> 11

import math

def SumDigitsNumber(number):
    sum = 0
    for x in str(number):
        if x == ',' or x == '-' or x == '.':
            x = 0
        sum += int(x)

    print(sum)


n = float(input())
SumDigitsNumber(n)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

# Реализуйте алгоритм перемешивания списка.