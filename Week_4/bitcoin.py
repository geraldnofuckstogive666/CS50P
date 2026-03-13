#https://cs50.harvard.edu/python/psets/4/bitcoin/


import sys
import requests


URL = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=3c4f4900f45b12eccee5cb5b5fe821b3b6fb455eae0fc53c9e03c9b3b7996638"


def fetch_price(url: str) -> float:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    response_json = response.json()
    return float(response_json['data']['priceUsd'])


def main():
    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
        except ValueError:
            sys.exit("Command line argument is not a number")
    else:
        sys.exit("Missing command-line argument")

    price = fetch_price(URL)
    if not price:
        sys.exit('Error')

    print(f"${price * n:,.4f}")


if __name__ == "__main__":
    main()
