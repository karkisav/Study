import emoji

def main():
    text = input("Input: ")
    if not emoji.is_emoji(text):
        print("Output: " + emoji.emojize(text, language="alias"))
    else:
        print("Output: " + emoji.demojize(text,language="alias"))
main()