class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Logger(metaclass=SingletonMeta):
    def log(self, message):
        print(f"Log: {message}")

# Client code
logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)  # Output: True
logger1.log("This is a singleton logger.")
