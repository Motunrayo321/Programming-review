def main():
    time = input("What is the time? ")
    converted_time = convert(time)

    hour, minutes = converted_time.split('.')

    match hour:
        case '7' | '8':
            print ("Time for breakfast")
        case '12' | '13':
            print ("Time for lunch")
        case '18' | '19':
            print ("Time for dinner")
        case _:
            print ("It's not time for any meal!")


def convert(time):
    hour, minute = time.split(':')
    minute = int(minute)
    hour = int (hour)

    decimal = (f"{hour + (minute/60)}")
    return decimal


if __name__ == "__main__":
    while True:
        main()



