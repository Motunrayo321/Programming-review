def main():
    balance = 50

    print ("Please insert only 25 cents, 10 cents, or 5 cents.\n")

    while balance > 0:
        print (f"Amount due: {balance}")

        amount = int(input("Insert coin: "))

        if amount == 25 or amount == 10 or amount == 5:
            balance -= amount
        else:
            print ("Invalid amount!")
    
    change = -balance
    print (f"Change owed: {change}")

main()