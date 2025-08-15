class LoggingMockUserDatabase:
    def __init__(self, user_data):
        self.user_data = user_data
        self.calls = []

    def get_user_data(self, user_id):
        self.calls.append(user_id)
        return self.user_data.get(user_id, {'age': 0})

    def verify_calls(self, user_id):
        return user_id in self.calls
