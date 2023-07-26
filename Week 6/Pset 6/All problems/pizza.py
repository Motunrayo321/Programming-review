from lines import argv_check
from tabulate import tabulate
import csv
import sys


def main():
    argv_check('csv', 1)

    header = ['Sicilian Pizza', 'Small' ,'Large']

    file_name = sys.argv[1]
    table = file_return(file_name, header)

    print (tabulate(table, headers='firstrow', tablefmt='grid'))
    


def file_return(file_name, header):
    actual_file = []

    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file, fieldnames=header)
            #print (reader)

            for line in reader:
                actual_file.append(line)
        
    except FileNotFoundError:
        sys.exit("This file does not exist in this directory!")
            
    #print (actual_file)

    return actual_file


if __name__ == "__main__":
    main()