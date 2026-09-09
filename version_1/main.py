from functions import calculate
from config import OPERATORS


operator = OPERATORS
print("Добро пожаловать!")

while True:

    try:

        a = float(input("Введите первое число: "))

        while True:
            operation = input("Введите действие: ")

            if operation in operator:
                break

            print("Такой операции нету!")        
        
        b = float(input("Введите второе число: "))

        if a < b:
            print("Первое число не может быть меньше второго!")
            continue

        result = calculate(a , operation, b)
        print(f"Результат: {result} ")

    except ValueError:
        print("Введите число!")

    except ZeroDivisionError: 
        print("Нельзя делить на ноль!")