class UserService:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def register_user(self, user):
        # logic for registering a user
        self.notification_service.send_notification(f"User {user} registered successfully!")
notification_service = NotificationService()
user_service = UserService(notification_service)
user_service.register_user("Alice")
