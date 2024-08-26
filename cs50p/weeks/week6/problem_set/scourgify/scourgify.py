import csv
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    try:
        filename1 = sys.argv[1].split(".")
        filename2 = sys.argv[2].split(".")
        filenames = [filename1, filename2]
        for filename in filenames:
            if len(filename) != 2 or filename[1] != "csv":
                sys.exit(f"Could not read {filename[0]}.csv")

        sourgify(sys.argv[1], sys.argv[2])
    except FileNotFoundError:
        sys.exit("File does not exist")

def sourgify(read_file, write_file):
    students = []
    with open(read_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["name"] = [name.strip() for name in row["name"].split(",")]
            students.append({"first": row["name"][1], "last": row["name"][0], "house": row["house"]})

    with open(write_file, "w") as file:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader() 
        writer.writerows(students)
if __name__ == "__main__":
    main()