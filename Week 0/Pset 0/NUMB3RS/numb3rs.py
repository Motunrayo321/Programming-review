import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match := re.search(r"^((?:[0-2]?[0-5]?[0-5]{1})|(?:[0-1]?[0-9]?[0-9]{1})\.){3}((?:[0-2]?[0-5]?[0-5]{1})|(?:[0-1]?[0-9]?[0-9]{1})\.){3}$", ip):
        print (True)
        return (match.group(1))





if __name__ == "__main__":
    main()