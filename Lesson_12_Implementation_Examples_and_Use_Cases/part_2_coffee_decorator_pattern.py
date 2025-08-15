class Coffee:
    def cost(self):
        return 5  # base cost for a simple coffee
class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1.5  # cost after adding milk
class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 0.5  # cost after adding sugar
plain_coffee = Coffee()
print(f"Plain coffee cost: ${plain_coffee.cost()}")

coffee_with_milk = MilkDecorator(plain_coffee)
print(f"Coffee with milk cost: ${coffee_with_milk.cost()}")

coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
print(f"Coffee with milk and sugar cost: ${coffee_with_milk_and_sugar.cost()}")
