def main():
    expression = input("Expression: ").split()
    if len(expression) != 3:
        return -1
    else:
        answer = calc(expression)
        print(answer)

def calc(expression):
    x = float(expression[0])
    y = expression[1]
    z = float(expression[2])

    if y == '+':
        return x + z
    elif y == '-':
        return x - z
    elif y == '*':
        return x * z
    elif y == '/':
        return round(x / z, 1)
main()