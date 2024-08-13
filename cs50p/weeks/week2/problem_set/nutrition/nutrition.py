def main():
    food = input("Item: ")
    calories(food)

raw_fruits = {
    "Apple": "130",
    "Avocado": "50",
    "Banana": "110",
    "Cantaloupe": "50",
    "Grapefruit": "60",
    "Grapes": "90",
    "Honeydew Melon": "50",
    "Kiwifruit": "90",
    "Lemon": "15",
    "Lime": "20",
    "Nectarine": "60",
    "Orange": "80",
    "Peach": "60",
    "Pear": "100",
    "Pineapple": "50",
    "Plums": "70",
    "Strawberries": "50",
    "Sweet Cherries": "100",
    "Tangerine": "50",
    "Watermelon": "80",
}

raw_fruits = {key.lower(): value for key, value in raw_fruits.items()}

def calories(food):
    food = food.lower()
    if food in raw_fruits:
        print(f"Calories: {raw_fruits[food]}")
        return
    else:
        print("")

main()