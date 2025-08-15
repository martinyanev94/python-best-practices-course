def test_database_failure_handling():
    mock_db = FailingMockUserDatabase()
    user_stats = UserStatistics(mock_db)
    
    try:
        user_stats.calculate_average_age([1, 2, 3])
    except Exception as e:
        assert str(e) == "Database not available.", "Expected failure message not raised."
