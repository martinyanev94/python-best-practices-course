class UserDatabase:
    def get_user_data(self, user_id):
        raise NotImplementedError("This method should be overridden.")
class UserStatistics:
    def __init__(self, database):
        self.database = database

    def calculate_average_age(self, user_ids):
        total_age = 0
        for user_id in user_ids:
            user_data = self.database.get_user_data(user_id)
            total_age += user_data['age']
        return total_age / len(user_ids)
