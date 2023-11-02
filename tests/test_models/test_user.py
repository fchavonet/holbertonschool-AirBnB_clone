#!/usr/bin/python3

"""
Module with unittests for User class.
"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test class for User class.
    """

    def test_1_create_user(self):
        """
        Test if attributes are initialized to empty strings.
        """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_2_set_user_attributes(self):
        """
        Test setting the attributes of a User instance.
        """
        user = User()
        user.email = "batman@batcave.com"
        user.password = "iloverobin"
        user.first_name = "Bruce"
        user.last_name = "Wayne"

        self.assertEqual(user.email, "batman@batcave.com")
        self.assertEqual(user.password, "iloverobin")
        self.assertEqual(user.first_name, "Bruce")
        self.assertEqual(user.last_name, "Wayne")

    def test_3_user_instance_of_base_model(self):
        """
        Test if a User instance is also an instance of BaseModel.
        """
        user = User()
        self.assertIsInstance(user, BaseModel)


if __name__ == "__main__":
    unittest.main()
