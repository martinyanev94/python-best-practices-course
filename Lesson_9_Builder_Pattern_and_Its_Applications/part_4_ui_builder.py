class UIComponent:
    def __init__(self, component_type):
        self.component_type = component_type
        self.properties = {}

    def set_property(self, name, value):
        self.properties[name] = value

    def __str__(self):
        return f"{self.component_type} with properties {self.properties}."


class UIBuilder:
    def __init__(self):
        self.components = []

    def add_component(self, component_type):
        component = UIComponent(component_type)
        self.components.append(component)
        return component

    def build(self):
        return self.components


# Client code
ui_builder = UIBuilder()
button = ui_builder.add_component("Button")
button.set_property("color", "green")
button.set_property("size", "large")

label = ui_builder.add_component("Label")
label.set_property("text", "Welcome!")

components = ui_builder.build()
for component in components:
    print(component)
