from typing import Optional

from eth_typing import Hash32
from web3 import Web3

from tickers import BaseTicker


class EthereumTicker(BaseTicker):
    confirmations_count = 50

    def __init__(self, connection_string):
        self.rpc_connection = Web3(Web3.HTTPProvider(connection_string))
        assert self.rpc_connection.isConnected()

    @staticmethod
    def make_configuration(rpc_user: Optional[str], rpc_password: Optional['str'], ip_address: Optional[str],
                           port: Optional[int]):
        return dict(connection_string=f'http://{ip_address}:{port}')

    def get_transaction(self, transaction_hash: str):
        return self.rpc_connection.eth.get_transaction(Hash32(transaction_hash))

    def get_last_block_number(self) -> int:
        return self.rpc_connection.eth.block_number

    def was_transaction_confirmed(self, transaction_hash: str) -> bool:
        transaction = self.get_transaction(transaction_hash)
        count = self.get_last_block_number() - transaction['blockNumber']
        return count >= self.confirmations_count
