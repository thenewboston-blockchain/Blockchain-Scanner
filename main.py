class Scanner:

    def __init__(self, ticker, amount, receiving_address, expiration_time):
        self.ticker = ticker  # BTC or ETH
        self.amount = amount
        self.receiving_address = receiving_address
        self.expiration_time = expiration_time
        self.status = 'PENDING'

    def start(self):
        """
        This will start scanning the given blockchain (Bitcoin or Ethereum) until the transaction is confirmed or until
        the expiration time is reached.
        """

        while self.status == 'PENDING':

            # Query BTC or ETH blockchain to see if `self.amount` has been sent to `self.receiving_address` yet

            if transaction_confirmed:
                self.status = 'CONFIRMED'
                print('Confirmed')
                break

            if now() > self.expiration_time:
                self.status = 'EXPIRED'
                print('Expired')
                break


if __name__ == '__main__':
    scanner = Scanner(
        ticker='BTC',
        amount=0.05,  # BTC
        receiving_address='3PXqf3tZkq5VsbtaVkVfioxRRVdbdF3bP3',
        expiration_time='2021-11-07 14:37:32.308930'
    )
    scanner.start()
