class Character:
    def __init__(self, name):
        self.name = name

    def display(self):
        return f"Character: {self.name}"
class CharacterFactory:
    def __init__(self):
        self.characters = {}

    def get_character(self, name):
        if name not in self.characters:
            self.characters[name] = Character(name)
        return self.characters[name]
factory = CharacterFactory()

hero1 = factory.get_character("Hero")
hero2 = factory.get_character("Hero")  # this will be the same instance as hero1

print(hero1.display())
print(hero2.display())

print(f"Are both hero1 and hero2 the same object? {'Yes' if hero1 is hero2 else 'No'}")
