def main():
    text = input("Input: ")
    print(f"Output: {shorten(text)}", end="")

def shorten(text):
    vowels = ['a', 'e', 'o', 'u', 'i']
    new_text = ""
    for i in range(len(text)):
        if text[i] not in vowels:
            new_text += text[i]
    return new_text

if __name__ == "__main__":
    main()