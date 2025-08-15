class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)


class TechnicalSupport(Handler):
    def handle_request(self, request):
        if request == "Technical Issue":
            print("Technical Support: Handling technical issue.")
        else:
            super().handle_request(request)


class BillingSupport(Handler):
    def handle_request(self, request):
        if request == "Billing Issue":
            print("Billing Support: Handling billing issue.")
        else:
            super().handle_request(request)


class GeneralSupport(Handler):
    def handle_request(self, request):
        print(f"General Support: Handling request for '{request}'.")


# Setting up the chain of responsibility
tech_support = TechnicalSupport()
billing_support = BillingSupport()
general_support = GeneralSupport(tech_support)

# This chain will handle requests: General -> Technical
billing_support.handle_request("Technical Issue")
billing_support.handle_request("Billing Issue")
billing_support.handle_request("Other Request")
