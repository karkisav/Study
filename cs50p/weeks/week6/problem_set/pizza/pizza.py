import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    try:
        filename = sys.argv[1].split(".")
        if len(filename) != 2 or filename[1] != "csv":
            sys.exit("Not a CSV file")

        print(tabulate(menu(sys.argv[1]), tablefmt="grid", headers="keys"))
    except FileNotFoundError:
        sys.exit("File does not exist")
    

def menu(filename):
    menu = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            menu.append(row)
    return menu

if __name__ == "__main__":
    main()