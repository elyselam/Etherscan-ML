from etherscan.contracts import Contract
import json
import sys
import os

with open('../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']



def main():

    if len(sys.argv) < 2:
    	print("usage: " + os.path.basename(__file__) + " Smart Contract Address")
    	print("Smart Contracts can be found on ERC20 token pages and where they are used")
    	sys.exit(1)
    else:
    	wallet_addy = str(sys.argv[1])
    	address = wallet_addy
    	api = Contract(address=wallet_addy, api_key=key)
    	abi = api.get_abi()
    	# abi = int(abi) 

    print(abi)


main()
