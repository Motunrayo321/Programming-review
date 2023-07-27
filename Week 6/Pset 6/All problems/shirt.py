from lines import argv_check

from PIL import Image
from PIL import ImageOps
from os import path

import sys
import csv


def main ():
    argv_check(['image', 'jpg', 'jpeg', 'png'], 3, all_file=True)

    file = sys.argv[1]
    new_file = sys.argv[2]
    shirt = sys.argv[3]
    file_return(file, shirt, new_file)
    

def file_return(file_name, over_file, new_file):

    try:
        with Image.open(file_name) as file:
            print(file.size)
            file.show()

            fit_file = ImageOps.fit(file, (600,600))
            print(fit_file.size)
            fit_file.show()

            with Image.open(over_file) as shirt_file:
                print(shirt_file.size)
                shirt_file.show()

                fit_file.paste(shirt_file, shirt_file)
                fit_file.show()

                fit_file.save(new_file)
        
    except FileNotFoundError:
        sys.exit("This file does not exist in this directory!")
            
    #print (actual_file)

    #return actual_file


main ()