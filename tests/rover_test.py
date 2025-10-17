import unittest
from src.rover import execute

class TestExecute(unittest.TestCase):
    def test_no_command(self):
        self.assertTrue(execute("") == "0:0:N")

    def test_move_once(self):
        self.assertTrue(execute("M") == "0:1:N")

    def test_move_twice(self):
        self.assertTrue(execute("MM") == "0:2:N")

    def test_move_thrice(self):
        self.assertTrue(execute("MMM") == "0:3:N")

    def test_exceed_north(self):
        height = 10
        command = "M" * height
        self.assertTrue(execute(command, grid_height=height) == "0:0:N")