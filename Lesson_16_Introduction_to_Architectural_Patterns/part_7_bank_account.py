class BankAccount:
    def __init__(self):
        self.balance = 0
        self.events = []

    def apply_event(self, event):
        if event['type'] == 'deposit':
            self.balance += event['amount']
        elif event['type'] == 'withdraw':
            self.balance -= event['amount']
        self.events.append(event)
    
    def deposit(self, amount):
        self.apply_event({'type': 'deposit', 'amount': amount})

    def withdraw(self, amount):
        self.apply_event({'type': 'withdraw', 'amount': amount})
