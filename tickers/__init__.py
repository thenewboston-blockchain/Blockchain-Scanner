from typing import TypeVar, Type, Optional

from tickers.utils import import_from_string

T = TypeVar('T', bound='BaseTicker')


class BaseTicker:
    confirmations_count = None

    def __init__(self, connection_string: str):
        raise NotImplementedError('Must be implemented in a child class')

    @classmethod
    def get_instance(cls: Type[T], blockchain_type: str) -> T:
        return import_from_string(f'tickers.{blockchain_type}.{blockchain_type.capitalize()}Ticker')

    def __init__(self, *args, **kwargs):
        raise NotImplementedError('Must be implemented in a child class')

    @staticmethod
    def make_configuration(rpc_user: Optional[str], rpc_password: Optional['str'], ip_address: Optional[str],
                           port: Optional[int]):
        raise NotImplementedError('Must be implemented in a child class')

    def get_transaction(self, transaction_hash: str):
        raise NotImplementedError('Must be implemented in a child class')

    def get_last_block_number(self) -> int:
        raise NotImplementedError('Must be implemented in a child class')

    def was_transaction_confirmed(self, transaction_hash: str) -> bool:
        raise NotImplementedError('Must be implemented in a child class')
