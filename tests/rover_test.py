import unittest
import numpy as np
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

    def test_exceed_south(self):
        height = 10
        self.assertEqual(execute("RRM", grid_height=height), "0:9:S")

    def test_exceed_west(self):
        width = 10 
        self.assertEqual(execute("LM", grid_width=width), "9:0:W")

    def test_exceed_east(self):
        width = 10
        command = "R" + ("M" * width)
        self.assertEqual(execute(command, grid_width=width), "0:0:E")

    def test_turn_right(self):
        self.assertEqual(execute("R"), "0:0:E")

    def test_turn_right_twice(self):
        self.assertEqual(execute("RR"), "0:0:S")

    def test_clockwise_spin(self):
        self.assertEqual(execute("RRRR"), "0:0:N")

    def test_turn_left(self):
        self.assertEqual(execute("L"), "0:0:W")

    def test_left_twice(self):
        self.assertEqual(execute("LL"), "0:0:S")

    def test_anticlockwise_spin(self):
        self.assertEqual(execute("LLLL"), "0:0:N")
    
    def test_move_turn_move(self):
        self.assertEqual(execute("MRM"), "1:1:E")

    def test_circle(self):
        self.assertEqual(execute("MRMRMRMR"), "0:0:N")
        
    def test_obstacle_hit_from_bottom(self):
        obstacles = [np.array((1.0, 1.0))]
        self.assertEqual(execute("RMLM", obstacles=obstacles), "O:1:0:N")
        
    def test_obstacle_hit_from_left(self):
        obstacles = [np.array((1.0, 1.0))]
        self.assertEqual(execute("MRM", obstacles=obstacles), "O:0:1:E")

    def test_obstacle_hit_from_top(self):
        obstacles = [np.array((1.0, 1.0))]
        self.assertEqual(execute("MMRMRM", obstacles=obstacles), "O:1:2:S")

    def test_obstacle_hit_from_right(self):
        obstacles = [np.array((1.0, 1.0))]
        self.assertEqual(execute("RMMLMLM", obstacles=obstacles), "O:2:1:W")