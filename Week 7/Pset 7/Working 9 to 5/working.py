import re
import sys


def main():
    print(convert(input("Hours: ")))
    pass


def convert(s):
    """
    ([0-1][0-2])
    # ((?:[0-1][0-2]){2})
    ([0]?[0-9])
    #([0-1]?[0-9]{1})

    (([1][0-2])|([0]?[1-9]))

    ([0-5]?[0-9])
    ([0-5][0-9])
    (:[0-5]?[0-9])
    #(:[0-5]?[0-9]{1})
    # ([6][0]) Unnecessary
    #(([6][0]){2})

    # [AM|PM] incorrect
    (AM|PM)

    ((([1][0-2])|([0]?[1-9]))(:([0-5][0-9]))? ([AM|PM]))

    """
    if match := re.search(r"^(((?:[1][0-2])|(?:[0]?[1-9]))(?::([0-5][0-9]))? (AM|PM)) to (((?:[1][0-2])|(?:[0]?[1-9]))(?::([0-5][0-9]))? (AM|PM))$", s, re.IGNORECASE):
        
        start, end = match.group(1), match.group(5)

        start_dets = {
            'hour': match.group(2),
            'minute': match.group(3),
            'period': match.group(4)
            }

        end_dets = {
            'hour': match.group(6),
            'minute': match.group(7),
            'period': match.group(8)
            }

        print (f"{start} - {end}\n")
        print (start_dets)
        print (end_dets)
        print ()

        final = output ([start_dets, end_dets])
        return final


def output(working_time):
    for time in working_time:
        if time['period'].lower() == 'pm':
            time['hour'] = int(time['hour'])
            time['hour'] += 12
    
        if not time['minute']:
            time['minute'] = '00'
    
    start = working_time[0]
    end = working_time[1]

    return (f"{start['hour']}:{start['minute']} to {end['hour']}:{end['minute']}")



while True:
    if __name__ == "__main__":
        main()