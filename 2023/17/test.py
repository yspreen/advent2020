from main import same_dir

import unittest


class TestSameDir(unittest.TestCase):
    def test_straight_line_max_length(self):
        origin = {(0, 1): (0, 0), (0, 2): (0, 1), (0, 3): (0, 2)}
        self.assertTrue(same_dir((0, 3), (0, 4), origin))

    def test_straight_line_not_max_length(self):
        origin = {(0, 1): (0, 0)}
        self.assertFalse(same_dir((0, 0), (0, 1), origin))

    def test_change_direction_before_max(self):
        origin = {(0, 1): (0, 0), (1, 1): (0, 1)}
        self.assertFalse(same_dir((0, 1), (1, 1), origin))

    def test_no_previous_position(self):
        origin = {}
        self.assertFalse(same_dir((0, 0), (0, 1), origin))

    def test_different_direction_each_step(self):
        origin = {(0, 1): (0, 0), (1, 1): (0, 1), (1, 2): (1, 1)}
        self.assertFalse(same_dir((1, 1), (1, 2), origin))

    def test_looping_path(self):
        origin = {(0, 1): (0, 0), (0, 0): (0, 1)}
        self.assertFalse(same_dir((0, 0), (0, 1), origin))

    def test_path_with_max_length_greater_than_3(self):
        origin = {(0, 1): (0, 0), (0, 2): (0, 1), (0, 3): (0, 2), (0, 4): (0, 3)}
        self.assertTrue(same_dir((0, 4), (0, 5), origin, max_length=4))


if __name__ == "__main__":
    unittest.main()
