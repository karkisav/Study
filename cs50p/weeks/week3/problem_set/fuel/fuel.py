def main():
    frac = get_frac("Fraction: ")
    print(fuel(frac))

def fuel(value):
    value = round(value * 100)
    if value <= 1:
        return "E"
    elif value >= 99:
        return "F"
    else:
        return str(value) + "%"

def get_frac(prompt):
    while True:
        try:
            fraction = input(prompt).split("/")

            # these raise the value error
            frac_upper = int(fraction[0])
            frac_lower = int(fraction[1])

            # this raises the zero div error
            frac = frac_upper/frac_lower

            # reprompt the user if frac value is > 1
            if frac_upper > frac_lower:
                continue
        except (ValueError, ZeroDivisionError):
            pass
        else:
            return frac_upper/frac_lower
        
main()