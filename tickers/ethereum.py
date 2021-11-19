from eth_typing import Hash32
from web3 import Web3

from tickers import BaseTicker


class EthereumTicker(BaseTicker):
    confirmations_count = 50

    def __init__(self, connection_string):
        self.rpc_connection = Web3(Web3.HTTPProvider(connection_string))
        assert self.rpc_connection.isConnected()

    def get_transaction(self, transaction_hash: str) -> dict:
        return self.rpc_connection.eth.get_transaction(Hash32(transaction_hash))

    def get_last_block_number(self) -> int:
        return self.rpc_connection.eth.block_number

    def was_transaction_confirmed(self, transaction: dict) -> bool:
        count = self.get_last_block_number() - transaction['blockNumber']
        return count >= self.confirmations_count

    def validate_amount(self, transaction: dict, amount: float):
        return float(transaction['value']) == amount

    def validate_receiving_address(self, transaction: dict, receiving_address: str):
        return transaction['scriptPubKey']['address'] == receiving_address
