import unittest
from snake import initialize_score, Scoreboard
class TestInitializeScore(unittest.TestCase):
    def test_initialize_score(self):
        self.assertEqual(initialize_score(), 0)
def initialize_score():
    return Scoreboard().current_score