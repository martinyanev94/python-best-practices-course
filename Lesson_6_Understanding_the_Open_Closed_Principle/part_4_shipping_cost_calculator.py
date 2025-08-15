class ShippingCostStrategy:
    def calculate_cost(self, weight):
        raise NotImplementedError("This method should be overridden.")

class StandardShippingCost(ShippingCostStrategy):
    def calculate_cost(self, weight):
        return weight * 1.0 

class ExpressShippingCost(ShippingCostStrategy):
    def calculate_cost(self, weight):
        return weight * 2.0 

class ShippingCostCalculator:
    def __init__(self, strategy: ShippingCostStrategy):
        self.strategy = strategy

    def calculate(self, weight):
        return self.strategy.calculate_cost(weight)
