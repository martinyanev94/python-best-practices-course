class NotificationService:
    def send_notification(self, message):
        print(f"Sending notification: {message}")

class UserService:
    def __init__(self):
        self.notification_service = NotificationService()

    def register_user(self, user):
        # logic for registering a user
        self.notification_service.send_notification(f"User {user} registered successfully!")
