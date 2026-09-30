import json
import requests
import sys


def main():

    if len(sys.argv) != 2:
        sys.exit("Missing Command-Line Argument")

    try:
        value = float(sys.argv[1])
    except ValueError:
        sys.exit("Command Line Argument in not a number")

    try:
        bitcoin = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=0a09a6410396f977e9fc9dfd2a7e47651906d5a8de0a2c3a3fb85af5d8b50a0d")
        bitcoin.raise_for_status()
        #print(json.dumps(bitcoin.json(), indent=2))

        data = bitcoin.json()

        result = value * float(data["data"]["priceUsd"])
        print(f"${result:,.4f}")


    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
