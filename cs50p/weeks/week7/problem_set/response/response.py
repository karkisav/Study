import validators
import sys

def main():
    print(valid_email(input("What's your email address? ")))

def valid_email(text):
    if validators.email(text):
        return "Valid"
    return "Invalid"

if __name__ == "__main__":
    main()