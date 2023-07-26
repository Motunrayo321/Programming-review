from lines import argv_check
from pizza import file_return
import sys
import csv
import json

def main():
    argv_check('csv', 2, all_file=True)

    before_header = ['name', 'house']
    after_header = ['first', 'last', 'house']

    before_file = sys.argv[1]   # file
    after_file = sys.argv[2]    # file

    prev_file = file_return(before_file, before_header)    # List of dicts

    #print (json.dumps(prev_file, indent=2))
    #print (len(prev_file))

    file_write(prev_file, after_file, after_header)


def file_write(array, new_file, header):
    """ Dict to file. """

    cur_file = []

    for row in array[1:]:
        #print (row)

        cur_dict = {}

        first, last = row['name'].split(', ')

        #print(first + '\n' + last)

        cur_dict['first'] = first
        cur_dict['last'] = last
        cur_dict['house'] = row['house']
        cur_file.append(cur_dict)
    
    #print ()
    #print (json.dumps(cur_file, indent=2))

    with open(new_file, 'a') as file:
        writer = csv.DictWriter(file, fieldnames=header)

        for item in cur_file:
            print (item)
            writer.writerow(item)


if __name__ == "__main__":
    main()