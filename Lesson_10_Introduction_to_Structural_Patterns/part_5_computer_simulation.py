class CPU:
    def freeze(self):
        print("CPU is frozen.")

    def jump(self, position):
        print(f"Jumping to position: {position}")

    def execute(self):
        print("Executing commands.")

class Computer:
    def __init__(self):
        self.cpu = CPU()

    def start(self):
        self.cpu.freeze()
        self.cpu.jump(100)
        self.cpu.execute()

# Usage
computer = Computer()
computer.start()
