class ShippingMethod:
    def calculate_cost(self, weight):
        raise NotImplementedError("This method should be overridden.")

class StandardShipping(ShippingMethod):
    def calculate_cost(self, weight):
        return weight * 1.0  # $1.0 per kg

class ExpressShipping(ShippingMethod):
    def calculate_cost(self, weight):
        return weight * 2.0  # $2.0 per kg

class InternationalShipping(ShippingMethod):
    def calculate_cost(self, weight):
        return weight * 3.5  # $3.5 per kg

class ShippingCostCalculator:
    def calculate_cost(self, shipping_method: ShippingMethod, weight):
        return shipping_method.calculate_cost(weight)
