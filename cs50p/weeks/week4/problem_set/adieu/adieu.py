import inflect

p = inflect.engine()

def main():
    list = adieu("Name:")
    print(f"Adieu, adieu, to {p.join(list)}")
    
def adieu(prompt):
    name_list = []
    while True:
        try:
            text = input(prompt)
            name_list.append(text)
        except EOFError:
            return name_list

main()