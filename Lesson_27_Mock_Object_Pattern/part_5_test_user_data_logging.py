def test_get_user_data_logging():
    user_data = {
        1: {'age': 25},
        2: {'age': 30},
    }
    mock_db = LoggingMockUserDatabase(user_data)
    user_stats = UserStatistics(mock_db)
    user_stats.calculate_average_age([1, 2])
    
    assert mock_db.verify_calls(1), "User ID 1 was not accessed."
    assert mock_db.verify_calls(2), "User ID 2 was not accessed."
