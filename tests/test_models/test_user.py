import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):

    def test_initialization(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_to_dict(self):
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], "")
        self.assertEqual(user_dict['password'], "")
        self.assertEqual(user_dict['first_name'], "")
        self.assertEqual(user_dict['last_name'], "")

    def test_initialization_with_parameters(self):
        email = "user@example.com"
        password = "password123"
        first_name = "John"
        last_name = "Doe"
        user_data = {
            'id': '123',
            'email': email,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'created_at': '2023-10-29T12:00:00',
            'updated_at': '2023-10-30T12:00:00'
        }
        user = User(**user_data)
        self.assertEqual(user.id, '123')
        self.assertEqual(user.email, email)
        self.assertEqual(user.password, password)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertEqual(user.created_at, datetime.strptime('2023-10-29T12:00:00', User.DATE_FORMAT))
        self.assertEqual(user.updated_at, datetime.strptime('2023-10-30T12:00:00', User.DATE_FORMAT))


if __name__ == '__main__':
    unittest.main()
