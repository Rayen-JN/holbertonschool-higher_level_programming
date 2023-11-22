#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
import io


class TestRectangleCases(unittest.TestCase):
    """
    Test cases for the Rectangle class methods.
    """

    def test_valid_constructor(self):
        """
        Test creating a valid Rectangle instance with a constructor.
        """
        rect = Rectangle(4, 5, 1, 2, 10)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 10)

    def test_invalid_width(self):
        """
        Test for TypeError when width is invalid (non-integer).
        """
        with self.assertRaises(TypeError):
            rect = Rectangle("invalid", 5)

    def test_negative_width(self):
        """
        Test for ValueError when width is negative.
        """
        with self.assertRaises(ValueError):
            rect = Rectangle(-1, 5)

    def test_invalid_height(self):
        """
        Test for TypeError when height is invalid (non-integer).
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(4, "invalid")

    def test_negative_height(self):
        """
        Test for ValueError when height is negative.
        """
        with self.assertRaises(ValueError):
            rect = Rectangle(4, -5)

    def test_invalid_x(self):
        """
        Test for TypeError when x is invalid (non-integer).
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(4, 5, "invalid")

    def test_negative_x(self):
        """
        Test for ValueError when x is negative.
        """
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 5, -1)

    def test_invalid_y(self):
        """
        Test for TypeError when y is invalid (non-integer).
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(4, 5, 1, "invalid")

    def test_negative_y(self):
        """
        Test for ValueError when y is negative.
        """
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 5, 1, -2)

    def test_area(self):
        """
        Test the area() method.
        """
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)

    def test_display(self):
        """
        Test the display() method.
        """
        rect = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        """
        Test the string representation of a Rectangle.
        """
        rect = Rectangle(4, 5, 1, 2, 10)
        expected_str = "[Rectangle] (10) 1/2 - 4/5"
        self.assertEqual(str(rect), expected_str)

    def test_update(self):
        """
        Test the update() method for Rectangle.
        """
        rect = Rectangle(4, 5, 1, 2, 10)
        rect.update(20)
        self.assertEqual(rect.id, 20)
        rect.update(20, 6, 7, 8, 9)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 8)
        self.assertEqual(rect.y, 9)

    def test_to_dictionary(self):
        """
        Test the to_dictionary() method for Rectangle.
        """
        rect = Rectangle(4, 5, 1, 2, 10)
        rect_dict = rect.to_dictionary()
        expected_dict = {
            'id': 10,
            'width': 4,
            'height': 5,
            'x': 1,
            'y': 2
        }
        self.assertEqual(rect_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
