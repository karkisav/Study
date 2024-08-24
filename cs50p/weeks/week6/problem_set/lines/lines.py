import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    try:
        filename = sys.argv[1].split(".")
        if len(filename) != 2 or filename[1] != "py":
            sys.exit("Not a python file")

        NumLines = lines(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(NumLines)

    
def lines(filename):
    count = 0
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if len(line) and not line.startswith("#"):
                count += 1
    return count


main()