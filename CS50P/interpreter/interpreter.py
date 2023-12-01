def sum(x, z):
    return x + z

def rest(x, z):
    return x - z

def multiply(x, z):
    return x * z

def divide(x, z):
    return x / z

def main():
    expression = input('Enter the expression ')
    x, y, z = expression.split(" ")

    if y == '+':
        print(sum(float(x), float(z)))
    elif y == '-':
        print(rest(float(x), float(z)))
    elif y == '*':
        print(multiply(float(x), float(z)))
    elif y == '/':
        print(divide(float(x), float(z)))

main()