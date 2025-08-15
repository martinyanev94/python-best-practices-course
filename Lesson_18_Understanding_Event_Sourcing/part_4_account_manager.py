class Account:
    def __init__(self, account_id):
        self.account_id = account_id
        self.balance = 0

    def load_events(self, events):
        for event in events:
            if event.event_type == "Deposit":
                self.balance += event.amount
            elif event.event_type == "Withdrawal":
                self.balance -= event.amount
events = [...] # Load events from the database for this specific account
account = Account(account_id=12345)
account.load_events(events)
print(f'Current balance for account {account.account_id}: {account.balance}')
