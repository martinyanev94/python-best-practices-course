class Command:
    def execute(self):
        pass


class OpenGate(Command):
    def execute(self):
        print("Opening the gate.")


class IncreaseTemperature(Command):
    def __init__(self, amount):
        self.amount = amount

    def execute(self):
        print(f"Increasing the temperature by {self.amount} degrees.")


class HomeAutomation:
    def parse_command(self, command_str):
        if command_str == "open gate":
            return OpenGate()
        elif command_str.startswith("increase temperature"):
            _, _, amount = command_str.split()
            return IncreaseTemperature(int(amount))


# Using the Interpreter pattern
automation = HomeAutomation()

# Simulating parsed commands
command = automation.parse_command("open gate")
command.execute()

command = automation.parse_command("increase temperature 5")
command.execute()
