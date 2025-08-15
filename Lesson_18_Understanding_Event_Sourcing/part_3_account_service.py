class AccountService:
    def __init__(self):
        self.account_balances = {}

    def handle_event(self, event):
        if event.event_type == "Deposit":
            self._apply_deposit(event)
        elif event.event_type == "Withdrawal":
            self._apply_withdrawal(event)

    def _apply_deposit(self, event):
        if event.account_id not in self.account_balances:
            self.account_balances[event.account_id] = 0
        self.account_balances[event.account_id] += event.amount

    def _apply_withdrawal(self, event):
        if event.account_id not in self.account_balances:
            self.account_balances[event.account_id] = 0
        self.account_balances[event.account_id] -= event.amount
