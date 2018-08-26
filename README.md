# Etherscan ML Machine Learning, Data Processing and Bash module 
This is an ongoing project.
Made by Elyse Lam for the USC Viterbi Data Science Bootcamp

Adapted from py-etherscan-api module by https://github.com/corpetty/

pip install etherscan-ml <br />
wget https://tinyurl.com/etherscan-ml <br />
MACOSX:  brew install gnu-sed <br />
<br />
# Scrape Etherscan then use Gephi to visualize network of transactions

<img src="/Network Analysis/EOS_network.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />


<br />
## wallet-tools
<br /><br />
<b>ether_balance.py</b> - Ether balance of a wallet.
<br /><br />
<b>wallet_inspector.py</b> - Experimental..discovered an undocumented API gets all transactions without paging issue get_all_transactions had. Requires additional formatting.
transaction_batch.py - Gets all of the 1st page transactions for a wallet. 
<br /><br />
## erc20-tools
<br /><br />
<b>get_abi.py</b> - Gets the abi of a smart contract. Fails for non-smart contracts. TODO: integrate with token test automation libraries
<br /><br />
<b>get_token_balance.py</b> - Gets the token balance of a wallet address. Useful to connect with data pulled from all_transactions.py
<br /><br />
<b>all_transactions.py</b>- Used to get all transactions for a Token. Must install gnu-sed (brew install gnu-sed) on Mac. Linux change gsed in fix_batch.sh to sed Python 3 only. Takes at least 20 mins to pull every transaction a token has ever had.
<br />			<b>Usage:</b> python3.6 all_transactions.py <token address> > tokenname.preprocessed
<br />			<b>(after completion):</b> ./fix_batch.sh tokenname.preprocessed
<br />			<b>(if you need a csv):</b> python3.6 convert-wallet.py <tokenname.json>
<br />			<b>Testing:</b> run ./fix_batch.sh medtoken.preprocessed for test data
<br />			<b>Notes:</b> ERC20 Transfers are buried inside of the data in the input field. 
<br />			This line works for a google sheets import of the CSV but I am working on a better tool. 
<br />			="0x"&LEFT(RIGHT($M4, 104), 40)   M is the location of input, and 4 is the row. The rest is charcount stripping.
<br />

## ether-tools
<br />
<b>get_ether_last_price.py</b> - Gets latest price.
<br /><br />
<b>get_total_ether_supply.py</b> - Gets total available ether in Ethereum Network.
<br />

Original py-etherscan-api was a well built scaffolding for python
scripts using the Etherscan API. The examples were so easy to work with
I created a very basic command line interface and a couple new tools and
decided to package them so you can integrate etherscan into your bash or
python scripts as an input or output.

Directories have been restructured to fit the tools better. I pipe
different wallet-tools into csvs for training or call them based on
triggers from bash scripts. Suggestions and requests welcome.

# Original Documentation Below:



EtherScan.io API python bindings

## Description
This module is written as an effort to provide python bindings to the EtherScan.io API, which can be found at: 
https://etherscan.io/apis
In order to use this, you must attain an Etherscan user account, and generate an API key.

In order to use the API, you must provide an API key at runtime, which can be found at the Etherscan.io API website.
If you'd like to use the provided examples without altering them, then the JSON file `api_key.json` must be stored in
the base directory.  Its format is as follows:

    { "key" : "YourApiKeyToken" }
    
with `YourApiKeyToken` is your provided API key token from EtherScan.io

## Installation
To install the package to your computer, simply run the following command in the base directory:

    python setup.py install

## Available bindings
Currently, only the following Etherscan.io API modules are available:

- accounts
- stats
- tokens

The remaining available modules provided by Etherscan.io will be added shortly

## Examples
All possible calls have an associated example file in the examples folder to show how to call the binding

These of course will be fleshed out with more details and explanation in time

Jupyter notebooks area also included in each directory to show all examples

## TODO:

- Package and submit to PyPI
- Add the following modules:
    - event logs
    - geth proxy
    - websockets
- Add robust documentation
- Add unit test suite
- Add request throttling based on Etherscan's suggestions

