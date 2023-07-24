import requests
import json
import sys

def main():
    try:
        num = sys.argv[1]

        value = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        real_value = value.json()['bpi']

        print (real_value)

    except ValueError:
        sys.exit("Invalid prompt!")

    except requests.RequestException:
        ...

main()