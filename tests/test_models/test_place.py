import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):

    def test_initialization(self):
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

    def test_to_dict(self):
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['city_id'], "")
        self.assertEqual(place_dict['user_id'], "")
        self.assertEqual(place_dict['name'], "")
        self.assertEqual(place_dict['description'], "")
        self.assertEqual(place_dict['number_rooms'], 0)
        self.assertEqual(place_dict['number_bathrooms'], 0)
        self.assertEqual(place_dict['max_guest'], 0)
        self.assertEqual(place_dict['price_by_night'], 0)
        self.assertEqual(place_dict['latitude'], 0.0)
        self.assertEqual(place_dict['longitude'], 0.0)
        self.assertEqual(place_dict['amenity_ids'], [])

    def test_initialization_with_parameters(self):
        city_id = "123"
        user_id = "456"
        name = "Cozy Cabin"
        place_data = {
            'id': '789',
            'city_id': city_id,
            'user_id': user_id,
            'name': name,
            'created_at': '2023-10-29T12:00:00',
            'updated_at': '2023-10-30T12:00:00'
        }
        place = Place(**place_data)
        self.assertEqual(place.id, '789')
        self.assertEqual(place.city_id, city_id)
        self.assertEqual(place.user_id, user_id)
        self.assertEqual(place.name, name)
        self.assertEqual(place.created_at, datetime.strptime('2023-10-29T12:00:00', Place.DATE_FORMAT))
        self.assertEqual(place.updated_at, datetime.strptime('2023-10-30T12:00:00', Place.DATE_FORMAT))


if __name__ == '__main__':
    unittest.main()
