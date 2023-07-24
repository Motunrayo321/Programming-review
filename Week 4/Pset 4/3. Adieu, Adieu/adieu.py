import inflect

p = inflect.engine()

def main():
    names = []

    while True:
        try:
            name = input("Which name would you lke to add? ")
            names.append(name.title())

        except (EOFError, KeyboardInterrupt):
            break
        
    print (f"Adieu, adieu to {p.join(names)}.")

main()