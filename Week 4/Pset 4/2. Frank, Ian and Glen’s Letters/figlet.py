import sys
import random
from pyfiglet import Figlet



def main():
    #print (len(sys.argv))

    if len(sys.argv) == 1:
        print (fonts(text, None))
    
    if len(sys.argv) == 3:
        if sys.argv[1] == '-f' or sys.argv[1] == '--font':
            print (fonts(text, sys.argv[2]))
        else:
            sys.exit("Invalid format!")
    
    text = input("Write your text here: ")
        

def fonts(text, type):
    figlet = Figlet()

    font_list = figlet.getFonts()

    if not type:
        type = random.choice(font_list)
    
    #print (font_list, '\n')
    #print (type)

    figlet.setFont(font=type)

    return figlet.renderText(text)


main()