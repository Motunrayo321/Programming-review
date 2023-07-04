def main():
    #dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    space, payment = d.split('$')
    payment = float(payment)
    print (payment)


def percent_to_float(p):
    tip_percent = p.replace('%', ' ')
    tip_percent = float(tip_percent) * 0.01
    print tip_percent
    #payment = float(payment)
    


main()