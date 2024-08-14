def main():
    get_price("Food: ")
    return

def get_price(Prompt):
    price = 0
    while True:
        try:
            item = input(Prompt).title()
            if item not in items:
                pass
            else:
                price += float(items[item])
                print(f"Total ${price:.2f}")
                pass
        except EOFError:
            return
        
items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

main()