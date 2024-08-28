import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(input):
    matches = re.fullmatch(r"([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)", input)
    if matches is None:
        return False
    for i in range(4):
        if not (0 <= int(matches.group(i+1)) <= 255):
            return False
    return True

if __name__ == "__main__":
    main()