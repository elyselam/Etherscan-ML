from  etherscan.tokens import Tokens
import json
import sys
import os

with open('../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']


def main():

    if len(sys.argv) < 2:
    	 print("usage: " + os.path.basename(__file__) + " user_wallet erc_20_contract_address")
    	 print("Find an ether wallet address. Whales can be found in the token holders section")
    	 sys.exit(1)
    elif len(sys.argv) < 3:
    	print("usage: " + os.path.basename(__file__) + " user_wallet ERC20_CONTRACT_ADDRESS") 
    	print("Find the ERC20 contract address. Click the token name in token transactions.")
    	sys.exit(1)
    else:
    	wallet_addy = str(sys.argv[1])
    	token_addy = str(sys.argv[2])
    	api = Tokens(contract_address=token_addy, api_key=key)
    	balance = api.get_token_balance(address=wallet_addy)
    	balance = int(balance) 

    	if (balance > 0):
           balance = balance / 1000000000000000000

    print(balance)


main()


