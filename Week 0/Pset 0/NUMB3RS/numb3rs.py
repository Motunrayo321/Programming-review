import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """
    ([0-2]?[0-5]?[0-5]{1})
    ([0-1]?[0-9]?[0-9]{1})
    """

    if match := re.search(r"^((?:[0-1]?[0-9]?[0-9]{1})|(?:[2]?[0-5]?[0-5]{1}))$", ip):
        print (True)
        return (match.group(1))




while True:
    if __name__ == "__main__":
       main()