def main():
    order = input("Enter your order: ").title()
    cost = 0

    while True:
        try:
            cost += order_check(order)

            if order_check(order) == 0:
                print (f"{order} is not an item on the menu!")
            else:
                print (f"${cost:.2f}")

            order = input("Anything else? ").title()

        except (EOFError, KeyboardInterrupt):
            print (f"\nThank you for coming! \nYour total is: ${cost:.2f}")
            break


def order_check(order):

    menu = {

        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }

    if order in menu:
        return menu[order]
    else:
        return 0


main()