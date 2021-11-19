from tickers import BaseTicker
from tickers.nodes.nano_node import NanoNode


class NanoTicker(BaseTicker):
    confirmations_count = 50

    def __init__(self, connection_string):
        self.rpc_connection = NanoNode(connection_string)

    def get_transaction(self, transaction_hash: str):
        return self.rpc_connection.get_block_info(transaction_hash)

    def was_transaction_confirmed(self, transaction: dict) -> bool:
        return transaction['confirmed'] == 'true'

    def validate_amount(self, transaction: dict, amount: float):
        return float(transaction['amount']) == amount

    def validate_receiving_address(self, transaction: dict, receiving_address: str):
        return transaction['contents']['account'] == receiving_address
