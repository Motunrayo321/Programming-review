import sys

def line_check():
    file_name = sys.argv[1]

    with open(file_name, 'r') as file:
        for line in file:
            print(line.strip())

line_check()