from etherscan.accounts import Account
import json
import sys
import os
import pprint

with open('../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']


def main():

    if len(sys.argv) < 2:
    	print("usage: " + os.path.basename(__file__) + " user_wallet")
    	sys.exit(1)
    else:
    	wallet_addy = str(sys.argv[1])
    	address = wallet_addy
    	api = Account(address=wallet_addy, api_key=key)
    	transaction_page = api.get_transaction_page(page=1, offset=10000, sort='des')
  
    pprint.pprint(transaction_page)

main()
