import unittest
from src.rover import execute

class TestExecute(unittest.TestCase):
    def test_no_command(self):
        self.assertTrue(execute("") == "0:0:N")

    def test_move_once(self):
        self.assertTrue(execute("M") == "0:1:N")
