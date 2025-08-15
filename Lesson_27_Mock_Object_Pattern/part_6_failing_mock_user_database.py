class FailingMockUserDatabase:
    def get_user_data(self, user_id):
        raise Exception("Database not available.")
