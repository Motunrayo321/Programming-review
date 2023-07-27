from lines import argv_check

from PIL import Image
from PIL import ImageOps
from os import path

import sys
import csv


def main ():
    argv_check(['image', 'jpg', 'jpeg', 'png'], 2, all_file=True)

    file = sys.argv[1]
    shirt = sys.argv[2]
    file_return(file, shirt)
    

def file_return(file_name, over_file):

    try:
        with Image.open(file_name) as file:
            print(file.size)
            file.show()

            ImageOps.fit(file, (600,600))
            print(file.size)
            file.show()

            with Image.open(over_file) as shirt_file:
                print(shirt_file.size)
                shirt_file.show()

                #ImageOps.fit(file, (500,500))
        
    except FileNotFoundError:
        sys.exit("This file does not exist in this directory!")
            
    #print (actual_file)

    #return actual_file


main ()