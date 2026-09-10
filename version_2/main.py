from functions import calculate
from config import OPERATORS

def get_number(message):

    while True:
        try:
            return float(input(message))
        
        except ValueError:
            print("Введите число!")

def get_operation():

    while True:
        operaion = input("Введите действие: ")

        if operaion in OPERATORS:
            return operaion

        print("Такой операции нету!")

def main():

    is_running = True

    print("Добро пожаловать!")

    while is_running:

        a = get_number("Введите первое число: ")
        operation = get_operation()
        b = get_number("Введите второе число: ")

        try:

            result = calculate(a , operation, b)
            print(f"Результат: {result}")
            

        except ZeroDivisionError:
            print("На ноль делить нельзя!")

        answer = input("Хотите продолжить(да/нет): ").strip()
        
        if answer == "да":
            print("Хорошо")
        else:
            is_running = False
            print("Пока")
            
main()