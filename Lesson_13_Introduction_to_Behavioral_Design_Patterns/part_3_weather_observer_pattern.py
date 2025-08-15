class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = None

    def register_observer(self, observer):
        self._observers.append(observer)

    def unregister_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify_observers()


class DisplayDevice:
    def update(self, temperature):
        print(f"Display updated with new temperature: {temperature}°C")


class WeatherApp:
    def update(self, temperature):
        print(f"Weather App updated with new temperature: {temperature}°C")


# Using the Observer pattern
station = WeatherStation()
display = DisplayDevice()
app = WeatherApp()

station.register_observer(display)
station.register_observer(app)

# Simulate a temperature change
station.set_temperature(25)
station.set_temperature(30)
