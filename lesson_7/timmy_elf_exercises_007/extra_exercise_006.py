# Lambda

def calc_input():
    input_formula = input("Enter calculation (e.g. '5 * 7' or '7 / 2'): ")
    parts = input_formula.split(" ")
    a = int(parts[0])
    op = parts[1]
    b = int(parts[2])
    return a, op, b

operations = {
    "+": lambda a,b: a + b,
    "-": lambda a,b: a - b,
    "*": lambda a,b: a * b,
    "/": lambda a,b: a / b,
    "%": lambda a,b: a % b
}

def calculate(op):
    return operations[op]

a, op, b = calc_input()
print(calculate(op)(a, b))