class PaymentProcessor:
    def process_payment(self, payment_type, amount):
        if payment_type == 'credit_card':
            return f"Processed {amount} using Credit Card."
        # Additional payment types can be added here
class PaymentMethod:
    def process_payment(self, amount):
        raise NotImplementedError("This method should be overridden.")

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processed {amount} using Credit Card."

class PaypalPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processed {amount} using PayPal."

class PaymentProcessor:
    def process_payment(self, payment_method: PaymentMethod, amount):
        return payment_method.process_payment(amount)
