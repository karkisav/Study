try:
    x = input(input("Type your number"))
except ValueError:
    print("x is NOT an Int please put an Int (Integer)")
else:
    print(f"x is {x}")