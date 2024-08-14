def main():
    dict = get_items("")
    for item in sorted(dict.keys()):
        print(f"{dict[item]} {item}")
    return

def get_items(prompt):
    items = {}
    while True:
        try: 
            key = input(prompt).upper()
            if key in items:
                items[key] += 1
            else:
                items[key] = 1

        except EOFError:
            return items
        
main()