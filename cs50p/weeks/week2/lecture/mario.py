def main():
    print_square(4)

def print_square(size):
        for _ in range(size):   
            print_row(size)

def print_row(width):
       print("#" * width)
main()