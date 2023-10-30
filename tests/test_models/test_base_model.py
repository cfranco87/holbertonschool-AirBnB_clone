import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def test_initialization(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_save(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_initialization_with_parameters(self):
        created_at = '2023-10-29T12:00:00'
        updated_at = '2023-10-30T12:00:00'
        model_data = {
            'id': '123',
            'created_at': created_at,
            'updated_at': updated_at
        }
        model = BaseModel(**model_data)
        self.assertEqual(model.id, '123')
        self.assertEqual(model.created_at, datetime.strptime(created_at, BaseModel.DATE_FORMAT))
        self.assertEqual(model.updated_at, datetime.strptime(updated_at, BaseModel.DATE_FORMAT))


if __name__ == '__main__':
    unittest.main()
