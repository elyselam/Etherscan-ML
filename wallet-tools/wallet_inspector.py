from etherscan.mldatamodels import DataModels
import json
import sys
import pprint
import os

with open('../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']


def main():

    if len(sys.argv) < 3:
    	print("usage: " + os.path.basename(__file__) + " user_wallet contract_address")
    	print("Find the token transactions of a wallet for a token.")
    	sys.exit(1)
    else:

    	wallet_addy = str(sys.argv[1])
    	token_addy = str(sys.argv[2])
    	api = DataModels(contract_address=token_addy, api_key=key)
    	balance = api.get_token_transactions(address=wallet_addy)

    pprint.pprint(balance)
    #TODO: Cleanup output automatically. 
    #For now just use find/replace or pipe to a file and strip.

main()
