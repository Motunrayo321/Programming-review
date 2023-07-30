import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r"https?://(?:www\.)?youtube.com/embed(\w*)", s):
        url = match.group(1)
        return f"https://youtu.be/{url}"


while True:
    if __name__ == "__main__":
        main()