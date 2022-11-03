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


# n = float(input())
# SumDigitsNumber(n)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def ListFactorial(number):
    s = []
    y = 1
    for x in range(1, number+1):
        s.append(y*x) 
        y *= x
    print(s)


# nn = int(input())
# ListFactorial(nn)



# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

def ListSequence (number):
    s = []
    for k in range(1, number+1):
        s.append((1+1/k)** k) 
    print(sum(s))



# nn = int(input())
# ListSequence(nn)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].

def ListElements (number):
    s = []
    for k in range(0, number*2+1):
        s.append(number*(-1)+k) 
    print(s)

    y = 1
    for x in input("Введите через пробел позиции элементов: "):
        x = int(x)
        if x != ' ' and x < len(s):
            y *= s[x-1]
        elif x > len(s):
            print("Введенный номер позиции выходит за границы массива.")
    print(y)

nn = int(input())
ListElements(nn)


# Найдите произведение элементов на указанных пользователем через пробел позициях.

# Реализуйте алгоритм перемешивания списка.