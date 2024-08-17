import random


def main():
    level = get_level()
    total_score = 10
    error = 0
    for _ in range(10):
        wrong_attempt = 0
        int_1 = generate_integer(level=level)
        int_2 = generate_integer(level=level)

        answer = int_1 + int_2

        try:
            attempt = input(f"{int_1} + {int_2} = ")
        except EOFError:
            return

        if attempt != str(answer):
            wrong_attempt += 1
            print("EEE")
            for _ in range(2):
                attempt = input(f"{int_1} + {int_2} = ")
                if attempt != str(answer):
                    wrong_attempt += 1
                    print("EEE")
                else:
                    break
        if wrong_attempt == 3:
            print(f"{int_1} + {int_2} = {answer}")
            error += 1
    print(f"Score: {total_score - error}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                pass
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)
    


if __name__ == "__main__":
    main()