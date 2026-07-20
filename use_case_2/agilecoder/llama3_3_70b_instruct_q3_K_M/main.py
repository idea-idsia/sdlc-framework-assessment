'''
The TestService1 class that provides unit tests for the Service1 class.
'''
import unittest
from service1 import Service1
from database import Database
class TestService1(unittest.TestCase):
    def setUp(self):
        self.db = Database("test_application.db")
        self.service1 = Service1(self.db)
    def test_get_ticket_categories(self):
        # Arrange and Act
        categories = self.service1.get_ticket_categories()
        # Assert
        self.assertIsNotNone(categories)
if __name__ == "__main__":
    unittest.main()