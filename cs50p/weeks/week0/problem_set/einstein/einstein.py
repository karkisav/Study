def main():
    mass = int(input("m: "))
    E = energy(mass)
    print(E)

def energy(mass):
    return pow(300000000, 2) * mass

main()