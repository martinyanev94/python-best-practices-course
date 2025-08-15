import unittest

class TestPaymentProcessor(unittest.TestCase):
    def test_credit_card_payment(self):
        processor = PaymentProcessor()
        payment = CreditCardPayment()
        result = processor.process_payment(payment, 100)
        self.assertEqual(result, "Processed 100 using Credit Card.")

    def test_paypal_payment(self):
        processor = PaymentProcessor()
        payment = PaypalPayment()
        result = processor.process_payment(payment, 200)
        self.assertEqual(result, "Processed 200 using PayPal.")

if __name__ == '__main__':
    unittest.main()
