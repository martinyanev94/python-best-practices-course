class ShippingCostCalculator:
    def calculate_cost(self, method, weight):
        if method == 'standard':
            return weight * 1.0  # $1.0 per kg
        elif method == 'express':
            return weight * 2.0  # $2.0 per kg
        else:
            raise ValueError("Unknown shipping method")
