import requests
import sys
# Crypto Price Calculator
# This Python script fetches cryptocurrency prices using the CoinCap API and calculates total value based on user input.

# Replace ENTER_API_KEY_HERE with your own CoinCap API key
my_url = "https://rest.coincap.io/v3/assets?apiKey=ENTER_API_KEY_HERE"

def main():
    coin = get_coin()
    number = get_number()
    response = get_api_data(my_url)
    try:
        content = response.json()
    except ValueError:
       sys.exit("Invalid API response.")
    coin_dict = None
    for dictionary in content["data"]:
        if dictionary.get("symbol") == coin:
            coin_dict = dictionary # gets dict with desired coin
            break
    if coin_dict is None: # invalid coin case or not top 100 coins
        print("Coin not found")
        sys.exit(1)
    price = float(coin_dict["priceUsd"])
    print(f"${number * price:,.4f}")


def get_number():
    while True:
        try:
            number = float(input("Enter how many coins you are calculating for: "))
            return number
        except ValueError:
            print("Enter a valid number.")


def get_coin():
    coin = input("Enter the ticker symbol of your coin: ").strip().upper()
    return coin


def get_api_data(url):
    try:
        data = requests.get(url)
        data.raise_for_status()
        return data
    except requests.RequestException:
        print("Error in handling site info.")
        sys.exit(1)


if __name__ == "__main__":
    main()
