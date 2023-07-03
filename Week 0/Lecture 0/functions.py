def main():
    hello()
    hello("man\n")

    greeting, title = hello(input("Name: ").capitalize()).split(" ")

    print (f"\n{greeting}")

def hello (name="World"):
    text = f"Hey {name}"
    print (text)
    return text


main()