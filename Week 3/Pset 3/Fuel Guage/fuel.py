def main():

    while True:

        amount = input("Meter reading: ")
        num, denum = amount.split("/")
        
        try:
            real_amount = int(num)/int(denum) * 100

            if real_amount <= 1:
                print ('E')
            elif real_amount >= 99:
                print ('F')
            else:
                print (f"{real_amount:.0f}%")
            break

        except (ValueError, ZeroDivisionError):
            print ("Invalid input!\n")


main()