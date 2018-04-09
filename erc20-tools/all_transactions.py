from etherscan.accounts import Account
import json
import sys

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
    	transactions = api.get_all_transactions(offset=10000, sort='des', internal=False)
    	pprint.pprint(transactions)

main()

