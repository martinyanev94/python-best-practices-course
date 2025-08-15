class MockUserDatabase:
    def __init__(self, user_data):
        self.user_data = user_data

    def get_user_data(self, user_id):
        return self.user_data.get(user_id, {'age': 0})
def test_calculate_average_age():
    user_data = {
        1: {'age': 25},
        2: {'age': 30},
        3: {'age': 35}
    }
    mock_db = MockUserDatabase(user_data)
    user_stats = UserStatistics(mock_db)
    average_age = user_stats.calculate_average_age([1, 2, 3])
    
    assert average_age == 30, f"Expected 30 but got {average_age}"
