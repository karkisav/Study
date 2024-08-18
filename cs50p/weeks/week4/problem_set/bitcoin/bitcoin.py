import requests
import sys

def main():
    ammount = bitcoin_price()
    return print(f"${ammount:,.4f}")
def bitcoin_price():
    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")

        try:
            value = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")

        if float(sys.argv[1]) < 0:
            sys.exit("Command-line argument Can't be nagative")
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        response_Currencies = response["bpi"]
        response_USD = response_Currencies["USD"]
        return float(response_USD["rate_float"]) * float(sys.argv[1])
    except (requests.RequestException, ValueError):
        return

main()