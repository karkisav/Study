while True:
    try:
        x = input(input("Type your number"))
    except ValueError:
        print("x is NOT an Int please put an Int (Integer)")
    else:
        break
    
print(f"x is {x}")