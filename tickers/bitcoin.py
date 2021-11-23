from bitcoinrpc.authproxy import AuthServiceProxy

from tickers import BaseTicker


class BitcoinTicker(BaseTicker):
    confirmations_count = 3

    def __init__(self, connection_string):
        self.rpc_connection = AuthServiceProxy(connection_string)

    def get_transaction(self, transaction_hash: str):
        return self.rpc_connection.gettxout(transaction_hash, 0)

    def was_transaction_confirmed(self, transaction: dict) -> bool:
        return transaction['confirmations'] >= self.confirmations_count

    def validate_amount(self, transaction: dict, amount: float):
        return float(transaction['value']) == amount

    def validate_receiving_address(self, transaction: dict, receiving_address: str):
        return transaction['scriptPubKey']['address'] == receiving_address
