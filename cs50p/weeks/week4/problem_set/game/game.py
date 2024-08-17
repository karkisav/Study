import random
import sys

def main():
    guess("Level: ")
    return

def guess(prompt):
    while True:
        try:
            level = int(input(prompt))
            rand_int = random.randint(0, level)
            guess_value = int(input("Guess: "))
            if guess_value < 0 or level < 0:
                pass
            if guess_value < rand_int:
                print("Too small!")
                pass
            if guess_value > rand_int:
                print("Too large!")
                pass
            if guess_value == rand_int:
                sys.exit("Just right!")
                
        except ValueError:
            pass

main()