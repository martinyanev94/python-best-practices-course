class Account:
    def __init__(self, account_id):
        self.account_id = account_id
        self.balance = 0

    def snapshot(self):
        return {
            'account_id': self.account_id,
            'balance': self.balance,
            'timestamp': datetime.datetime.now()
        }

    def load_snapshot(self, snapshot):
        self.balance = snapshot['balance']
