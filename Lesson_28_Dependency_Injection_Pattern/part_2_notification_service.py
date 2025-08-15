from abc import ABC, abstractmethod

class INotificationService(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass
class EmailNotificationService(INotificationService):
    def send_notification(self, message):
        print(f"Email sent: {message}")

class SMSNotificationService(INotificationService):
    def send_notification(self, message):
        print(f"SMS sent: {message}")
def main():
    email_service = EmailNotificationService()
    sms_service = SMSNotificationService()

    user_service_email = UserService(email_service)
    user_service_sms = UserService(sms_service)

    user_service_email.register_user("Alice")
    user_service_sms.register_user("Bob")

if __name__ == "__main__":
    main()
