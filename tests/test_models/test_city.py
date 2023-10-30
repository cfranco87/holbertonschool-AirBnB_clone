import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):

    def test_initialization(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_to_dict(self):
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['state_id'], "")
        self.assertEqual(city_dict['name'], "")

    def test_initialization_with_parameters(self):
        state_id = "123"
        name = "New York"
        city_data = {
            'id': '456',
            'state_id': state_id,
            'name': name,
            'created_at': '2023-10-29T12:00:00',
            'updated_at': '2023-10-30T12:00:00'
        }
        city = City(**city_data)
        self.assertEqual(city.id, '456')
        self.assertEqual(city.state_id, state_id)
        self.assertEqual(city.name, name)
        self.assertEqual(city.created_at, datetime.strptime('2023-10-29T12:00:00', City.DATE_FORMAT))
        self.assertEqual(city.updated_at, datetime.strptime('2023-10-30T12:00:00', City.DATE_FORMAT))


if __name__ == '__main__':
    unittest.main()
