from config import OPERATORS

def calculate(a, operation, b):
    return OPERATORS[operation](a,b)