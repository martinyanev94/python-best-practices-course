import copy

class Website:
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain

    def __str__(self):
        return f'Website: {self.name}, Domain: {self.domain}'

# Prototype
class Prototype:
    def __init__(self):
        self.registry = {}

    def register(self, name, obj):
        self.registry[name] = obj

    def clone(self, name, **attrs):
        clone = copy.deepcopy(self.registry.get(name))
        if clone is None:
            raise ValueError(f"No prototype found for {name}.")
        for key, value in attrs.items():
            setattr(clone, key, value)
        return clone

# Usage
prototype = Prototype()
website1 = Website("Python", "python.org")
prototype.register("python", website1)

website2 = prototype.clone("python", name="Django", domain="djangoproject.com")
print(website1)
print(website2)
