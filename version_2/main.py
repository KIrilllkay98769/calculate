from functions import calculate
from config import OPERATORS

def get_number(message):
    while True:
        try:
            return float(input(message))
        
        except ValueError:
            print("Введите число!")

def get_operaion():

    while True:
        operaion = input("Введите действие: ")

        if operaion in OPERATORS:
            return operaion

        print("Такой операции нету!")

def main():

    print("Добро пожаловать!")

    while True:

        a = get_number("Введите первое число: ")
        operation = get_operaion()
        b = get_number("Введите второе число: ")

        try:

            result = calculate(a , operation, b)
            print(f"Результат: {result}")
            break

        except ZeroDivisionError:
            print("На ноль делить нельзя!")

main()