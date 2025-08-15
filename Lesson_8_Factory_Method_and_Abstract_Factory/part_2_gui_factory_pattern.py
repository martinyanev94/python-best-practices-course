class Button:
    def paint(self):
        raise NotImplementedError("This method should be overridden.")

class WindowsButton(Button):
    def paint(self):
        return "Rendering a Windows button."

class MacOSButton(Button):
    def paint(self):
        return "Rendering a MacOS button."

class GUIFactory:
    def create_button(self):
        raise NotImplementedError("This method should be overridden.")

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

# Client code
def get_ui(factory: GUIFactory):
    button = factory.create_button()
    return button.paint()

# Usage
windows_factory = WindowsFactory()
print(get_ui(windows_factory))

mac_factory = MacOSFactory()
print(get_ui(mac_factory))
