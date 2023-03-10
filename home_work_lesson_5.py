# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

print("Задача 26")
a26 = int(input("A: "))
b26 = int(input("B: "))

def rec(a,b):
    if b <= 0:
        return 1
    return a * rec(a, b-1)

print(rec(a26,b26))

# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

print("Задача 28")
a28 = int(input("A: "))
b28 = int(input("B: "))

def sum(a,b):
    if b <= 0:
        return a
    return sum(a + 1, b-1)

print(sum(a28,b28))