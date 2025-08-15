class MockNotificationService(INotificationService):
    def __init__(self):
        self.messages_sent = []

    def send_notification(self, message):
        self.messages_sent.append(message)
def test_register_user():
    mock_service = MockNotificationService()
    user_service = UserService(mock_service)
    user_service.register_user("Charlie")

    assert "User Charlie registered successfully!" in mock_service.messages_sent

test_register_user()
