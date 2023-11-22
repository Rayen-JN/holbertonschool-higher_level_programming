#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquareCases(unittest.TestCase):
    """
    Test cases for the Square class methods.
    """

    def test_valid_constructor(self):
        """
        Test creating a valid Square instance with a constructor.
        """
        square = Square(4, 1, 2, 10)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.id, 10)

    def test_invalid_size(self):
        """
        Test for TypeError when size is invalid (non-integer).
        """
        with self.assertRaises(TypeError):
            square = Square("invalid", 2, 3, 10)

    def test_negative_size(self):
        """
        Test for ValueError when size is negative.
        """
        with self.assertRaises(ValueError):
            square = Square(-1, 2, 3, 10)

    def test_invalid_x(self):
        """
        Test for TypeError when x is invalid (non-integer).
        """
        with self.assertRaises(TypeError):
            square = Square(4, "invalid", 3, 10)

    def test_negative_x(self):
        """
        Test for ValueError when x is negative.
        """
        with self.assertRaises(ValueError):
            square = Square(4, -2, 3, 10)

    def test_invalid_y(self):
        """
        Test for TypeError when y is invalid (non-integer).
        """
        with self.assertRaises(TypeError):
            square = Square(4, 2, "invalid", 10)

    def test_negative_y(self):
        """
        Test for ValueError when y is negative.
        """
        with self.assertRaises(ValueError):
            square = Square(4, 2, -3, 10)

    def test_str(self):
        """
        Test the string representation of a Square.
        """
        square = Square(4, 1, 2, 10)
        expected_str = "[Square] (10) 1/2 - 4"
        self.assertEqual(str(square), expected_str)

    def test_update(self):
        """
        Test the update() method for Square.
        """
        square = Square(4, 1, 2, 10)
        square.update(20)
        self.assertEqual(square.id, 20)
        square.update(20, 6, 7, 8)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_to_dictionary(self):
        """
        Test the to_dictionary() method for Square.
        """
        square = Square(4, 1, 2, 10)
        square_dict = square.to_dictionary()
        expected_dict = {
            'id': 10,
            'size': 4,
            'x': 1,
            'y': 2
        }
        self.assertEqual(square_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
