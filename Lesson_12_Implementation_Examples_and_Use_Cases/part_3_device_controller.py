class RemoteControl:
    def turn_on(self):
        raise NotImplementedError("This method should be overridden.")

    def turn_off(self):
        raise NotImplementedError("This method should be overridden.")
class Television(RemoteControl):
    def turn_on(self):
        return "Television is now ON."

    def turn_off(self):
        return "Television is now OFF."

class Radio(RemoteControl):
    def turn_on(self):
        return "Radio is now ON."

    def turn_off(self):
        return "Radio is now OFF."
class DeviceController:
    def __init__(self, device: RemoteControl):
        self._device = device

    def operate(self):
        print(self._device.turn_on())
        print(self._device.turn_off())
tv_controller = DeviceController(Television())
radio_controller = DeviceController(Radio())

tv_controller.operate()
radio_controller.operate()
