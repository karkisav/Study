def main():
    num = get_int()
    print(f"x is {num}")

def get_int():    
    while True:
        try:
           return int(input("Type your number"))
        except ValueError:
            print("x is NOT an Int please put an Int (Integer)")

main()