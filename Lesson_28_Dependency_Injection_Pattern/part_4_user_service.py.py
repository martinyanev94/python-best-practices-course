class UserService:
    def register_user(self, user, notification_service):
        # logic for registering a user
        notification_service.send_notification(f"User {user} registered successfully!")
