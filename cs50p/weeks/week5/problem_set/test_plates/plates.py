def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    #verifying length
    str_len = len(s)
    if str_len > 6 or str_len <= 2:
        return False
    
    # starts with two letters
    if not s[:2].isalpha():
        return False
        
    # check if number in between letters
    check_num_start = False

    for i in range(2, str_len):
        if s[i].isnumeric() and check_num_start == False:
            if s[i] == '0':
                return False
            check_num_start = True
        
        if i < str_len - 1:
            if s[i].isnumeric() and (s[i + 1].isalpha() or s[i + 1] == '.'):
                return False

    return True


if __name__ == "__main__":
    main()