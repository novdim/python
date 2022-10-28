# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def WeekendOrWeekday(number):
    if number == 6 or number == 7:
        print("Да")
    else:
        print("Нет")

print("Введите цифру от 1 до 7")
input_number = int(input())
WeekendOrWeekday(input_number)