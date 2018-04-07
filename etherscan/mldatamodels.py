from .client import Client


class DataModels(Client):
    def __init__(self, contract_address, api_key='YourApiKeyToken'):
        Client.__init__(self, address='', api_key=api_key)
        # self.url_dict[self.TOKEN_NAME] = tokenname
        self.url_dict[self.TRANSACTION_ADDRESS] = contract_address


    def get_token_transactions(self, address):
        self.url_dict[self.ADDRESS] = address
        self.url_dict[self.MODULE] = 'account'
        self.url_dict[self.ACTION] = 'txlist'
        self.build_url()
        req = self.connect()
        return req['result']

