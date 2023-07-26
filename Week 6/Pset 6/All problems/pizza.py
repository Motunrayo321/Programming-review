from lines import argv_check
from tabulate import tabulate
import csv
import sys

def main():
    argv_check('csv')

    header = ['Sicilian Pizza', 'Small' ,'Large']

    file_name = sys.argv[1]
    table = file_table(file_name, header)

    print (tabulate(table, headers='firstrow', tablefmt='grid'))

def file_table(file_name, header):
    actual_file = []

    with open(file_name, 'r') as file:
        reader = csv.DictReader(file, fieldnames=header)

        for line in reader:
            actual_file.append(line)
            
    print (actual_file)

    return actual_file


if __name__ == "__main__":
    main()