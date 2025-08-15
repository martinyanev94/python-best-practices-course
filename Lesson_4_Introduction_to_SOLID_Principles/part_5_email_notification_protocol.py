class Email:
    def send_email(self, message):
        print(f"Sending email: {message}")

class Notification:
    def __init__(self):
        self.email = Email()

    def send(self, message):
        self.email.send_email(message)
from typing import Protocol

class MessageSender(Protocol):
    def send(self, message: str):
        ...

class Email:
    def send(self, message: str):
        print(f"Sending email: {message}")

class Notification:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def send(self, message: str):
        self.sender.send(message)

if __name__ == "__main__":
    email = Email()
    notification = Notification(sender=email)
    notification.send(message="This is the message.")
