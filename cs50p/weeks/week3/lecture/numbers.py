def main():
    num = get_int("Type your number")
    print(f"x is {num}")

def get_int(prompt):    
    while True:
        try:
           return int(input(prompt))
        except ValueError:
            print("x is NOT an Int please put an Int (Integer)") #or just use pass

main()