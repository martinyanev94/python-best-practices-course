class LazyImage:
    def __init__(self, image_path):
        self.image_path = image_path
        self._image = None

    def load(self):
        if self._image is None:
            print(f"Loading image from {self.image_path}...")
            self._image = self._load_image_from_disk()
        return self._image

    def _load_image_from_disk(self):
        time.sleep(1)  # Simulating disk loading time
        return f"Image data for {self.image_path}"

lazy_image = LazyImage("path/to/image.jpg")
print("Image not yet loaded.")
print(lazy_image.load())  # Loads the image.
print("Image loaded again:", lazy_image.load())  # Fetches already loaded image.
