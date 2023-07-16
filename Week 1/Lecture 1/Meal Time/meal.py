def main():
    time = input("What is the time? ")

    if time.endswith('a.m.') or time.endswith('p.m.'):
        converted_time = new_convert(time)
    else:
        converted_time = convert(time)

    hour, minutes = converted_time.split('.')

    match hour:
        case '7':
            print ("Time for breakfast")
        case '12':
            print ("Time for lunch")
        case '18':
            print ("Time for dinner")
        case _:
            print ("It's not time for any meal!")


def convert(time):
    hour, minute = time.split(':')
    minute = int(minute)
    hour = int (hour)

    decimal = (f"{hour + (minute/60)}")
    print (decimal)
    return decimal

def new_convert (time):
    time_stamp, meridian = time.split(' ')
    hour, minute = time_stamp.split(':')
    minute = int(minute)
    hour = int (hour)

    if meridian == 'p.m.':
        hour += 12

    decimal = (f"{hour + (minute/60)}")
    print (decimal)
    return decimal



if __name__ == "__main__":
    while True:
        main()