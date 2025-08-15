class Image:
    def display(self):
        raise NotImplementedError("This method should be overridden.")
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"Loading image: {self.filename}")

    def display(self):
        print(f"Displaying image: {self.filename}")
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()
proxy_image = ProxyImage("example_image.jpg")

proxy_image.display()  # First call triggers loading
proxy_image.display()  # Subsequent call only displays
