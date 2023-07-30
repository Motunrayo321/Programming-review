import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    """
    ([0-2]?[0-5]?[0-5]{1})    [200-255] - "1/25/200/255"    Allows 1 and 2 digits but optimising seems pointless
    ([0-1]?[0-9]?[0-9]{1})    [0-199] - "1/25/99/100/199"

    ((?:[0-1]?[0-9]?[0-9]{1})|(?:[2]?[0-5]?[0-5]{1}))    [0-255] - "0/1/99/100/199/200/255"
    ((?:(?:[0-1]?[0-9]?[0-9]{1})|(?:[2]?[0-5]?[0-5]{1}))\.)     [x.] - "1./255."        
    ((?:(?:(?:[0-1]?[0-9]?[0-9]{1})|(?:[2]?[0-5]?[0-5]{1}))\.){3})     [x.x.x.] - "1.1.1./255.255.255."    
    ((?:(?:(?:(?:[0-1]?[0-9]?[0-9]{1})|(?:[2]?[0-5]?[0-5]{1}))\.){3})(?:(?:[0-1]?[0-9]?[0-9]{1})|(?:[2]?[0-5]?[0-5]{1})))    [x.x.x.x] - "1.1.1.1/255.255.255.255"   
    """

    if match := re.search(r"^((((([0-1]?[0-9]?[0-9]{1})|(?:[2]?[0-5]?[0-5]{1}))\.){3})(([0-1]?[0-9]?[0-9]{1})|([2]?[0-5]?[0-5]{1})))$", ip):
        #print (match.group(1))
        return True


while True:
    if __name__ == "__main__":
       main()