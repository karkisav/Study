def main():
    text = input("")
    convert(text)

def convert(text):
    words = text.split()
    for word in words:
        if word == ':(':
            word = '🙁'
        elif word == ':)':
            word ='🙂'
        print(f"{word} ", end="")
        


main()