# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

from math import sqrt


def WeekendOrWeekday(number):
    if number == 6 or number == 7:
        print("Да")
    else:
        print("Нет")

print("Введите цифру от 1 до 7")
input_number = int(input())
WeekendOrWeekday(input_number)



# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def VerificationOfApproval():
    for x in [True,False]:
        for y in [True,False]:
            for z in [True,False]:
                print(x,'AND',y,'OR',z,'=',x and y or z)


VerificationOfApproval()

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:


# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def DefinitionQuarterPlane(input_X, input_Y):
    if input_X > 0 and input_Y > 0:
        print("1")
    elif input_X < 0 and input_Y > 0:
        print("2")
    elif input_X < 0 and input_Y < 0:
        print("3")
    elif input_X > 0 and input_Y < 0:
        print("4")

print("Введите координаты точки X ≠ 0")
input_X1 = int(input())
print("Введите координаты точки Y ≠ 0")
input_Y1 = int(input())

DefinitionQuarterPlane(input_X1,input_Y1)
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

n = int(input('input quarter number: '))

def RangeQuarter():
    if n < 1 or n > 4:
        print('Please, repeat the input')
    elif n == 1:
        print('x > 0 and y > 0')
    elif n == 2:
        print('x < 0 and y > 0')
    elif n == 3:
        print('x < 0 and y < 0')
    elif n == 4:
        print('x > 0 and y < 0')

RangeQuarter()
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.


def CalculationLengthSegment(x_A, y_A, x_B, y_B):
    print(f"Расстояние отрезка AB: {round(sqrt(((x_A - x_B)**2) + ((y_A - y_B)**2)), 2)}")
    
CalculationLengthSegment(3, 6, 2, 1)
CalculationLengthSegment(7, -5, 1, -1)

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) ->1`` 7,21

print('Введите координаты точки А:')
x_A = float(input('X: '))
y_A = float(input('Y: '))
print("Введите координаты точки B:")
x_B = float(input('X: '))
y_B = float(input('Y: '))

CalculationLengthSegment(x_A, y_A, x_B, y_B)
