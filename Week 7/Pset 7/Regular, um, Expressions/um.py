import re
import sys


def main():
    print(count(input("Text: ")))


def count(text):
    if match := re.findall(r"\bum\b", text, re.IGNORECASE):
        return (len(match))


while True:
    if __name__ == "__main__":
        main()