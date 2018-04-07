from etherscan.accounts import Account
import json
import sys
import os

with open('../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

def main():

    if len(sys.argv) < 2:
    	print("usage: " + os.path.basename(__file__) + " user_wallet")
    	print("Finds the ether balance of a wallet address.")
    	sys.exit(1)
    else:
    	wallet_addy = str(sys.argv[1])
    	address = wallet_addy
    	api = Account(address=wallet_addy, api_key=key)
    	balance = api.get_balance()
    	balance = int(balance) 

    	if (balance > 0):
           balance = balance / 1000000000000000000

    print(balance)


main()

