def main():
    text = input("camelCase: ")
    print(f"sanke_case: {snake_case(text)}")

def snake_case(text):
    for i in range(len(text)):
        if text[i].isupper():
            text = text.replace(text[i], "_" + text[i].lower())
    return text

main()