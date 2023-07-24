import requests
import json
import sys

def main():
    try:
        num = float(sys.argv[1])

        initial_price = check_price('USD')
        final_price = num * initial_price

        print (f"${final_price:,.4f}")

    except ValueError:
        sys.exit("Invalid prompt!")


def check_price(currency):
    try:
        value = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        total = json.dumps(value.json(), indent=2)
        real_value = float(value.json()['bpi'][currency]['rate_float'])

        print (total)
        #print (real_value)
        return real_value

    except requests.RequestException:
        sys.exit("No connection!")


main()