from lines import argv_check
from pizza import file_return
import sys
import json

def main():
    argv_check('csv', 2, all_file=True)

    header = ['name', 'house']

    before_file = sys.argv[1]
    after_file = sys.argv[2]

    prev_file = file_return(before_file, header)
    cur_file = {}

    #print (json.dumps(prev_file, indent=2))
    print (len(prev_file))

    for row in prev_file[1:]:
        print (row)

        first, last = row['name'].split(', ')

        print(first + '\n' + last)

        cur_file['first'] = first
        cur_file['last'] = last
        cur_file['house'] = row['house']
    
    print ()
    print (json.dumps(cur_file, indent=2))

    # with open(before_file, 'a') as file:
    #     writer = csv.DictWriter()

    #     writer.writerow()


if __name__ == "__main__":
    main()