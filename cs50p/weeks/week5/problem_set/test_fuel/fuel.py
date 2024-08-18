def main():
    frac = convert(input("Fraction: "))
    print(gauge(frac))

def gauge(percentage):
    try:
        if 0 <= percentage <= 1:
            return "E"
        elif 99 <= percentage <= 100:
            return "F"
        elif 1 < percentage < 99:
            return f"{int(percentage)}%"
        else:
            raise TypeError
    except TypeError:
        pass

def convert(text):
    try:
        fraction = text.split("/")
        if len(fraction) != 2:
            raise ValueError()

        # these raise the value error
        frac_upper = int(fraction[0])
        frac_lower = int(fraction[1])

        # this raises the zero div error
        if frac_lower == 0:
            raise ZeroDivisionError()

        if frac_lower <= 0 or frac_upper < 0:
            raise ValueError()

        frac = frac_upper/frac_lower

        if frac > 1:
            raise ValueError()
        
        return int(frac * 100)
    except (ValueError, ZeroDivisionError):
        raise
        
        
if __name__ == "__main__":
    main()