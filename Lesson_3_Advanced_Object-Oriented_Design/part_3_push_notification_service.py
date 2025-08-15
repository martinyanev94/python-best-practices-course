class PushNotificationService(NotificationService):
    def notify(self, message):
        print(f"Sending push notification: {message}")

# Usage
notification_service = PushNotificationService()
notification_service.notify("You've got a new message!")
