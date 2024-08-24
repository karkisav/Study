name = input("What is you name: ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")