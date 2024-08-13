def main():
    text = input("Input: ")
    print(f"Output: {truncate(text)}", end="")


def truncate(text):
    vowels = ['a', 'e', 'o', 'u', 'i']
    new_text = ""
    for i in range(len(text)):
        if text[i].lower() not in vowels:
            new_text += text[i]
    return new_text
main()