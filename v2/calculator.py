

def inputsanitization(x, y):
    if 0 <= x <= 999 and 0 <= y <= 999:
        return True
    else:
        print("Input must be a number between 0 and 999")


def add(x, y):
    if inputsanitization(x, y):
        return x + y


def subtract(x, y):
    if inputsanitization(x, y):
        return x - y


def multiply(x, y):
    if inputsanitization(x, y):
        return x * y


def divide(x, y):
    if inputsanitization(x, y):
        return x / y

