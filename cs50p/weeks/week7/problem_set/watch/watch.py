import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(input):
    matches = re.search(r"^<iframe.+https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+).+></iframe>$", input)
    if matches is not None:
        return "https://youtu.be/" + matches.group(1)
    else:
        return None

if __name__=="__main__":
    main()