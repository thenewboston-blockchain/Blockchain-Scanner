import argparse
from datetime import datetime, timedelta

from constants import BLOCKCHAINS, BITCOIN
from tickers import BaseTicker


class Scanner:

    def __init__(self, ticker, amount, receiving_address, tx_hash, expiration_time):
        self.ticker = ticker
        self.amount = amount
        self.receiving_address = receiving_address
        self.tx_hash = tx_hash
        self.expiration_time = expiration_time
        self.status = 'PENDING'

    def start(self):
        """
        This will start scanning the given blockchain (Bitcoin or Ethereum) until the transaction is confirmed or until
        the expiration time is reached.
        """

        while self.status == 'PENDING':

            if datetime.now() > self.expiration_time:
                self.status = 'EXPIRED'
                print('Expired')
                break

            transaction = self.ticker.get_transaction(self.tx_hash)
            self.ticker.validate_transaction(transaction, self.amount, self.receiving_address)

            if self.ticker.was_transaction_confirmed(transaction):
                self.status = 'CONFIRMED'
                print('Confirmed')
                break


def parse_arguments():
    parser = argparse.ArgumentParser(description='')

    parser.add_argument('-b', '--blockchain', type=str, choices=BLOCKCHAINS, default=BITCOIN,
                        help='Select blockchain network. Default: Bitcoin')
    parser.add_argument('-u', '--username', type=str, required=False, help='RPC username')
    parser.add_argument('-p', '--password', type=str, required=False, help='RPC password')
    parser.add_argument('-a', '--amount', type=float, required=True, help='Amount value was sent')
    parser.add_argument('-r', '--receiving-address', type=str, required=True, help='Destination address')
    parser.add_argument('-t', '--tx', type=str, required=True, help='Transaction hash')
    parser.add_argument('-e', '--expiration', type=int, default=30,
                        help='Expiration time in minutes. Default: 30 minutes')
    parser.add_argument('--ip', type=str, default='127.0.0.1',
                        help='IP address of Full Node. Default: 127.0.0.1')
    parser.add_argument('--port', type=int, default=8332,
                        help='TPC number of port. Default: 8332')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()

    ticker_class = BaseTicker.get_instance(args.blockchain)
    ticker_configuration = ticker_class.make_configuration(username=args.username, password=args.password,
                                                           ip_address=args.ip, port=args.port)
    selected_ticker = ticker_class(**ticker_configuration)

    scanner = Scanner(
        ticker=selected_ticker,
        amount=args.amount,
        receiving_address=args.receiving_address,
        tx_hash=args.tx,
        expiration_time=datetime.now() + timedelta(minutes=args.expiration)
    )
    scanner.start()
