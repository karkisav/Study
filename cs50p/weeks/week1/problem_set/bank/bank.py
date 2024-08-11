def main():
    response = input("Greeting: ").strip()
    response = response.lower()
    check(response)

def check(response):
    if 'hello' in response:
        print("$0")
        return
    if response[0] == 'h':
        print("$20")
        return
    print("$100")
    return
    
main()