class Remote:
    def operate(self):
        raise NotImplementedError("You should implement this method!")

class TV(Remote):
    def operate(self):
        return "TV is now on."

class Radio(Remote):
    def operate(self):
        return "Radio is playing music."

class Device:
    def __init__(self, remote):
        self.remote = remote

    def operate_device(self):
        return self.remote.operate()

# Usage
tv = TV()
radio = Radio()

device1 = Device(tv)
device2 = Device(radio)

print(device1.operate_device())
print(device2.operate_device())
