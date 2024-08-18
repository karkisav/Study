def main():
    response = input("Greeting: ")
    print(f"${value(response)}")

def value(response):
    if 'hello' in response:
        return 0
    if response[0] == 'h':
        return 20
    return 100
    
if __name__ == "__main__":
    main()