def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()
    if answer == '42' or answer.lower() == 'forty two' or answer.lower() == 'forty-two':
        print("Yes")
        return
    else:
        print("No")
        return
main()