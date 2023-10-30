import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_initialization(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

    def test_to_dict(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], "")

    def test_from_dict(self):
        amenity_data = {
            'id': '123',
            'created_at': '2023-10-29T12:00:00',
            'name': 'Swimming Pool'
        }
        amenity = Amenity(**amenity_data)
        self.assertEqual(amenity.id, '123')
        self.assertEqual(amenity.created_at, '2023-10-29T12:00:00')
        self.assertEqual(amenity.name, 'Swimming Pool')


if __name__ == '__main__':
    unittest.main()
