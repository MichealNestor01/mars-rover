import unittest
from src.rover import execute

class TestExecute(unittest.TestCase):
    def test_no_command(self):
        self.assertTrue(execute("") == "0:0:N")
