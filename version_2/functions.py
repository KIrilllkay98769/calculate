def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def perimetr(a,b):
    return 2 * (a + b)

def calculate(a, operaion, b):

    if operaion == "+":
        return add(a, b)

    elif operaion == "-":
        return subtract(a, b)

    elif operaion == "*":
        return multiply(a, b)

    elif operaion == "/":
        return divide(a, b)

    elif operaion == "p":
        return perimetr(a, b)

