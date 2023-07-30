import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    """
    ([0-1][0-2])
    # ((?:[0-1][0-2]){2})
    ([0]?[0-9])
    #([0-1]?[0-9]{1})

    (([1][0-2])|([0]?[1-9]))

    ([0-5]?[0-9])
    ([0-5][0-9])
    (:[0-5]?[0-9])
    #(:[0-5]?[0-9]{1})
    # ([6][0]) Unnecessary
    #(([6][0]){2})

    # [AM|PM] incorrect
    (AM|PM)

    ((([1][0-2])|([0]?[1-9]))(:([0-5][0-9]))? ([AM|PM]))

    """
    if match := re.search(r"^(((?:[1][0-2])|(?:[0]?[1-9]))(?::([0-5][0-9]))? (AM|PM)) to (((?:[1][0-2])|(?:[0]?[1-9]))(?::([0-5][0-9]))? (AM|PM))$", s, re.IGNORECASE):
        return (match.groups())




while True:
    if __name__ == "__main__":
        main()