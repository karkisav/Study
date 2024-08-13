try:
    x = input(input("Type your number"))
    print(f"x is {x}")
except ValueError:
    print("x is NOT an Int please put an Int (Integer)")