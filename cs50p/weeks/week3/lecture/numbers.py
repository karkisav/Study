def main():
    num = get_int()
    print(f"x is {num}")

def get_int():    
    while True:
        try:
            x = input(input("Type your number"))
        except ValueError:
            print("x is NOT an Int please put an Int (Integer)")
        else:
            return x

main()