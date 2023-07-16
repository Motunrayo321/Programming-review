def main():
    time = input("What is the time? ")

    if time.endswith('a.m.') or time.endswith('p.m.'):
        converted_time = new_convert(time)
    else:
        converted_time = convert(time)

    #hour, minutes = converted_time.split('.')
    #print (type(converted_time))

    if 7.0 <= converted_time <= 8.0:
        print ("Time for breakfast")
    elif 12.0 <= converted_time <= 13.0:
        print ("Time for lunch")
    elif 18.0 <= converted_time <= 19.0:
        print ("Time for dinner")
    else:
        print ("It's not time for any meal!")


def convert(time):
    hour, minute = time.split(':')
    minute = int(minute)
    hour = int (hour)

    decimal = hour + (minute/60)
    #print (f"1 {decimal}")
    return decimal

def new_convert (time):
    time_stamp, meridian = time.split(' ')
    hour, minute = time_stamp.split(':')
    minute = int(minute)
    hour = int (hour)

    if meridian == 'p.m.':
        hour += 12

    decimal = hour + (minute/60)
    #print (f"2 {decimal}")
    return decimal



if __name__ == "__main__":
    while True:
        main()