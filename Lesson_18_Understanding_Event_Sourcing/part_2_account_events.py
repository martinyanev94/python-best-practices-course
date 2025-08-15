class AccountEvent:
    def __init__(self, account_id, event_type, amount):
        self.account_id = account_id
        self.event_type = event_type
        self.amount = amount
        self.created_at = datetime.datetime.now()

class DepositEvent(AccountEvent):
    def __init__(self, account_id, amount):
        super().__init__(account_id, "Deposit", amount)

class WithdrawalEvent(AccountEvent):
    def __init__(self, account_id, amount):
        super().__init__(account_id, "Withdrawal", amount)
