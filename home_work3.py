
import math

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
list1 = [2, 3, 5, 9, 3] 

def SumOfOddListItems(list):
    print(sum(list[1::2]))

# SumOfOddListItems(list1)

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list2 = [2, 3, 4, 5, 6]

def MultiplicationListItems(list):
    new_list = [list[x] * list[-x-1] for x in range(0,math.ceil(len(list)/2))] 
    print(new_list)

# MultiplicationListItems(list2)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]

def DifferenceMaxMinFractionalParts(list, number_decimal_places):
    min = 1
    max = 0
    for x in list:
        if x%1 < min and x%1 != 0:
            min = x%1
        if x%1 > max:
            max = x%1
    print(round((max-min),number_decimal_places))

#DifferenceMaxMinFractionalParts(list,2)

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def DecimalToBinary(number):
    print('Преобразовать десятичное числов двоичное можно используя встроенную функцию bin срезав 2 первых символа')
    print(bin(number)[2:])

    print('Или делить каждый раз на 2 =)')
    numberb = ''
    while number > 0:
        numberb  += str(number % 2)
        number = number // 2
    print(numberb)

# DecimalToBinary(int(45))

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)


def Negafibonacci(n):
    list_negafibonacci = []
    for i in range(-n, n+1):
        print(i)
        if i >= 0:
            id_x = range(i+1)
            list = [0,1]
            for x in id_x[2:]:
                list.append(list[x-1] + list[x-2])
                print(list)
            list_negafibonacci.append(list[i])                 
        else:
            id_x = range((-(i-1))+1)
            list = [1,0]
            for x in id_x[2:]:
                list.append(list[x-2] - list[x-1])
                print(list)
            list.reverse()
            list_negafibonacci.append(list[i-2])         
    print(list_negafibonacci)

Negafibonacci(8)

