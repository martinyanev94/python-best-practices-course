import unittest
from unittest.mock import MagicMock

class TestEmailNotificationService(unittest.TestCase):
    def test_send_email(self):
        service = EmailNotificationService()
        service.send_email = MagicMock(return_value="Sending email: Test Message")

        response = service.send_email("Test Message")
        self.assertEqual(response, "Sending email: Test Message")

if __name__ == "__main__":
    unittest.main()
