class PaymentProcessor:
    def pay(self, amount):
        raise NotImplementedError("This method should be overridden.")
class PayPal:
    def process_payment(self, amount):
        return f"Processing ${amount} payment through PayPal."

class Stripe:
    def process_transaction(self, amount):
        return f"Processing ${amount} payment through Stripe."
class PayPalAdapter(PaymentProcessor):
    def __init__(self):
        self.paypal = PayPal()

    def pay(self, amount):
        return self.paypal.process_payment(amount)

class StripeAdapter(PaymentProcessor):
    def __init__(self):
        self.stripe = Stripe()

    def pay(self, amount):
        return self.stripe.process_transaction(amount)
def initiate_payment(processor: PaymentProcessor, amount):
    return processor.pay(amount)

paypal_processor = PayPalAdapter()
stripe_processor = StripeAdapter()

print(initiate_payment(paypal_processor, 100))
print(initiate_payment(stripe_processor, 150))
