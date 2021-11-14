from typing import Optional

from bitcoinrpc.authproxy import AuthServiceProxy

from tickers import BaseTicker


class BitcoinTicker(BaseTicker):
    confirmations_count = 3

    def __init__(self, connection_string):
        self.rpc_connection = AuthServiceProxy(connection_string)

    @staticmethod
    def make_configuration(rpc_user: Optional[str], rpc_password: Optional['str'], ip_address: Optional[str],
                           port: Optional[int]):
        return dict(connection_string=f'http://{rpc_user}:{rpc_password}@{ip_address}:{port}')

    def get_transaction(self, transaction_hash: str):
        return self.rpc_connection.gettxout(transaction_hash, 0)

    def was_transaction_confirmed(self, transaction_hash: str) -> bool:
        transaction = self.get_transaction(transaction_hash)
        return transaction['confirmations'] >= self.confirmations_count
