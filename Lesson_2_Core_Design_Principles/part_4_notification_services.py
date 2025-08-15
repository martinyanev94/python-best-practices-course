class NotificationService:
    def send_email(self, message):
        raise NotImplementedError

    def send_sms(self, message):
        raise NotImplementedError

class EmailNotificationService(NotificationService):
    def send_email(self, message):
        print(f"Sending email: {message}")

    def send_sms(self, message):
        # Not needed for EmailNotificationService
        pass

class SMSNotificationService(NotificationService):
    def send_email(self, message):
        # Not needed for SMSNotificationService
        pass

    def send_sms(self, message):
        print(f"Sending SMS: {message}")
class EmailService:
    def send_email(self, message):
        raise NotImplementedError

class SMSService:
    def send_sms(self, message):
        raise NotImplementedError

class EmailNotificationService(EmailService):
    def send_email(self, message):
        print(f"Sending email: {message}")

class SMSNotificationService(SMSService):
    def send_sms(self, message):
        print(f"Sending SMS: {message}")

email_service = EmailNotificationService()
email_service.send_email("Hello Email")

sms_service = SMSNotificationService()
sms_service.send_sms("Hello SMS")
