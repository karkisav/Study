def main():
    text = input("")
    texts = text.split()
    playback(texts)

def playback(texts):
    for text in texts:
        print(f"{text}...", end="")

main()
