from lines import argv_check
from pizza import file_return
import sys

def main():
        argv_check('csv', 2, all_file=True)

    try:
        header = ['name', 'house']

        file_name = sys.argv[1]
        file = file_return(file_name, header)

    
