class TextField:
    def render(self):
        raise NotImplementedError("This method should be overridden.")

class WindowsTextField(TextField):
    def render(self):
        return "Rendering a Windows text field."

class MacOSTextField(TextField):
    def render(self):
        return "Rendering a MacOS text field."

class GUIFactory:
    def create_button(self):
        raise NotImplementedError("This method should be overridden.")

    def create_text_field(self):
        raise NotImplementedError("This method should be overridden.")

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_text_field(self):
        return WindowsTextField()

class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_text_field(self):
        return MacOSTextField()

# Client code
def get_ui(factory: GUIFactory):
    button = factory.create_button()
    text_field = factory.create_text_field()
    return button.paint() + "\n" + text_field.render()

# Usage
windows_factory = WindowsFactory()
print(get_ui(windows_factory))

mac_factory = MacOSFactory()
print(get_ui(mac_factory))
