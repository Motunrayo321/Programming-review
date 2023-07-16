def main ():
    operation = input ("Write the equation here: ")

    x, sign, y = operation.split(' ')
    x = int(x)
    y = int(y)

    if sign == '+':
        print (x + y)
    elif sign == '-':
        print (x - y)
    elif sign == '*':
        print (x * y)
    elif sign == '/':
        print (x / y)


while True:
    main()