class Character:
    def attack(self):
        raise NotImplementedError

class Warrior(Character):
    def attack(self):
        return "Warrior attacks with a sword!"

class Mage(Character):
    def attack(self):
        return "Mage casts a fireball!"

class CharacterFactory:
    @staticmethod
    def create_character(character_type):
        if character_type == "warrior":
            return Warrior()
        elif character_type == "mage":
            return Mage()
        else:
            raise ValueError("Unknown character type")

# Example usage
character = CharacterFactory.create_character("warrior")
print(character.attack())
