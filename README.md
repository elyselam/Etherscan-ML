# etherscan magic - machine learning and bash module 
Made by Elyse Lam for the USC Viterbi Data Science Bootcamp
## Adapted from py-etherscan-api module by https://github.com/corpetty/


Original py-etherscan-api was a well built scaffolding for python 
scripts using the Etherscan API. The examples were so easy to work with 
I created a very basic command line interface and a couple new tools and 
decided to package them so you can integrate etherscan into your bash or 
python scripts as an input or output.

Directories have been restructured to fit the tools better. I pipe 
different wallet-tools into csvs for training or call them based on 
triggers from bash scripts. Suggestions and requests welcome.

All file names are optimized for tab completion and designed to 
integrate into other programs as piped input or output.

## wallet-tools

ether_balance.py - Ether balance of a wallet.
wallet_inspector.py - Experimental..discovered an undocumented API gets all transactions without paging issue get_all_transactions had. Requires additional formatting.
transaction_batch.py - Gets all of the 1st page transactions for a wallet. 

## erc20-tools

get_abi.py - Gets the abi of a smart contract. Fails for non-smart contracts. TODO: integrate with testing library
get_token_balance.py - Gets the token balance of a wallet address.

## ether-tools
get_ether_last_price.py - Does as its name indicates.
get_total_ether_supply.py - Same.



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


## Holla at ya' boy
BTC: 16Ny72US78VEjL5GUinSAavDwARb8dXWKG

ETH: 0x5E8047fc033499BD5d8C463ADb29f10f11165ed0
