class GrandParent:
    pass

class Parent(GrandParent):
    pass

class Child(Parent):
    pass
class Parent:
    pass

class Child:
    def __init__(self, parent):
        self.parent = parent
