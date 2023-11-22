#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class methods.
    """

    def test_init_with_id(self):
        """
        Test the initialization of Base with an ID.
        """
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_init_without_id(self):
        """
        Test the initialization of Base without providing an ID.
        """
        base = Base()
        self.assertEqual(base.id, 1)  # The default starting ID is 1

    def test_to_json_string(self):
        """
        Test the to_json_string method.
        """
        data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        json_string = Base.to_json_string(data)
        self.assertEqual(
            json_string,
            '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]')

    def test_to_json_string_with_empty_list(self):
        """
        Test the to_json_string method with an empty list.
        """
        data = []
        json_string = Base.to_json_string(data)
        self.assertEqual(json_string, '[]')

    def test_save_to_file(self):
        """
        Test saving data to a JSON file.
        """
        data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        Base.save_to_file(data)

    def test_from_json_string(self):
        """
        Test the from_json_string method.
        """
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        data = Base.from_json_string(json_string)
        self.assertEqual(
            data, [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}])

    def test_from_json_string_with_empty_string(self):
        """
        Test the from_json_string method with an empty JSON string.
        """
        json_string = '[]'
        data = Base.from_json_string(json_string)
        self.assertEqual(data, [])

    def test_create(self):
        """
        Test the create method.
        """
        data = {'id': 1, 'name': 'Alice'}
        instance = Base.create(**data)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.name, 'Alice')


if __name__ == '__main__':
    unittest.main()
