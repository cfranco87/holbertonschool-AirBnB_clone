import unittest
import os
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.user = User()
        self.place = Place()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.review = Review()

    def test_new(self):
        self.storage.new(self.user)
        key = "User." + self.user.id
        self.assertTrue(key in self.storage.all())

    def test_save(self):
        self.storage.new(self.place)
        self.storage.save()
        self.assertTrue(os.path.isfile(self.storage._FileStorage__file_path))

    def test_reload(self):
        self.storage.new(self.state)
        self.storage.save()
        self.storage.reload()
        key = "State." + self.state.id
        self.assertTrue(key in self.storage.all())


if __name__ == '__main__':
    unittest.main()
