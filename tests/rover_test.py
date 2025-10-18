import unittest
from src.rover import execute

class TestExecute(unittest.TestCase):
    def test_no_command(self):
        self.assertEqual(execute(""), "0:0:N")

    def test_move_once(self):
        self.assertEqual(execute("M"), "0:1:N")

    def test_move_twice(self):
        self.assertEqual(execute("MM"), "0:2:N")

    def test_move_thrice(self):
        self.assertEqual(execute("MMM"), "0:3:N")

    def test_exceed_north(self):
        height = 10
        command = "M" * height
        self.assertEqual(execute(command, grid_height=height), "0:0:N")

    def test_turn_right(self):
        self.assertEqual(execute("R"), "0:0:E")