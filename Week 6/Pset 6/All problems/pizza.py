from lines import argv_check
from tabulate import tabulate
import csv
import sys

def main():
    argv_check('csv')

    file_name = sys.argv[1]
    table = file_table(file_name)

    print (table)

def file_table(file_name):
    actual_file = []

    with open(file_name, 'r') as file:
        reader = csv.DictReader(file, fieldnames=['Sicilian Pizza', 'Small' ,'Large'])

        for line in reader:
            actual_file.append(line)

    return actual_file

    
main()