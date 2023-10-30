import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):

    def test_initialization(self):
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, 'name'))

    def test_to_dict(self):
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], "")

    def test_initialization_with_parameters(self):
        name = "California"
        state_data = {
            'id': '123',
            'name': name,
            'created_at': '2023-10-29T12:00:00',
            'updated_at': '2023-10-30T12:00:00'
        }
        state = State(**state_data)
        self.assertEqual(state.id, '123')
        self.assertEqual(state.name, name)
        self.assertEqual(state.created_at, datetime.strptime('2023-10-29T12:00:00', State.DATE_FORMAT))
        self.assertEqual(state.updated_at, datetime.strptime('2023-10-30T12:00:00', State.DATE_FORMAT))


if __name__ == '__main__':
    unittest.main()
