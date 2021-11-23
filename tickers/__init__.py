from typing import TypeVar, Type, Optional

from exceptions import ValidationError
from tickers.utils import import_from_string

T = TypeVar('T', bound='BaseTicker')


class BaseTicker:
    confirmations_count = None

    def __init__(self, connection_string: str, receiving_address: str, amount: float):
        self.receiving_address = receiving_address
        self.amount = amount

    @classmethod
    def get_instance(cls: Type[T], blockchain_type: str) -> T:
        return import_from_string(f'tickers.{blockchain_type}.{blockchain_type.capitalize()}Ticker')

    def __init__(self, *args, **kwargs):
        raise NotImplementedError('Must be implemented in a child class')

    @staticmethod
    def make_configuration(username: Optional[str], password: Optional['str'], ip_address: Optional[str],
                           port: Optional[int]):
        credentials = ''
        if username:
            credentials += username
        if password:
            credentials += f':{password}'
        if credentials:
            credentials += '@'
        return dict(connection_string=f'http://{credentials}{ip_address}:{port}')

    def get_transaction(self, transaction_hash: str):
        raise NotImplementedError('Must be implemented in a child class')

    def get_last_block_number(self) -> int:
        raise NotImplementedError('Must be implemented in a child class')

    def was_transaction_confirmed(self, transaction: dict) -> bool:
        raise NotImplementedError('Must be implemented in a child class')

    def validate_transaction(self, transaction: dict, amount: float, receiving_address: str):
        errors = []
        if transaction is None:
            errors.append('tx hash is not present in blockchain')
        else:
            if not self.validate_receiving_address(transaction, receiving_address):
                errors.append('Destination address of transaction is invalid.')
            if not self.validate_amount(transaction, amount):
                errors.append('Amount is incorrect.')
        if errors:
            raise ValidationError(errors)

    def validate_amount(self, transaction: dict, amount: float):
        raise NotImplementedError('Must be implemented in a child class')

    def validate_receiving_address(self, transaction: dict, receiving_address: str):
        raise NotImplementedError('Must be implemented in a child class')
