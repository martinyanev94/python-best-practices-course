class UserService:
    def __init__(self):
        self.notification_service = None

    def register_user(self, user):
        if not self.notification_service:
            raise Exception("Notification service must be set!")
        # logic for registering a user
        self.notification_service.send_notification(f"User {user} registered successfully!")
