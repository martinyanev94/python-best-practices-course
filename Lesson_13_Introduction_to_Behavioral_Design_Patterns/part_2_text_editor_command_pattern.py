class Command:
    def execute(self):
        pass

    def undo(self):
        pass


class AddTextCommand(Command):
    def __init__(self, editor, text):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.add_text(self.text)

    def undo(self):
        self.editor.remove_text(len(self.text))


class TextEditor:
    def __init__(self):
        self.content = ""

    def add_text(self, text):
        self.content += text
        print(f"Text added: '{self.content}'")

    def remove_text(self, length):
        self.content = self.content[:-length]
        print(f"Text removed: '{self.content}'")


class CommandManager:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()


# Using the Command pattern
editor = TextEditor()
command_manager = CommandManager()

command_add_hello = AddTextCommand(editor, "Hello")
command_add_world = AddTextCommand(editor, " World")

command_manager.execute_command(command_add_hello)
command_manager.execute_command(command_add_world)

# Undo the last command
command_manager.undo()
