import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):

    def test_initialization(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_to_dict(self):
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['place_id'], "")
        self.assertEqual(review_dict['user_id'], "")
        self.assertEqual(review_dict['text'], "")

    def test_initialization_with_parameters(self):
        place_id = "123"
        user_id = "456"
        text = "Great place to stay!"
        review_data = {
            'id': '789',
            'place_id': place_id,
            'user_id': user_id,
            'text': text,
            'created_at': '2023-10-29T12:00:00',
            'updated_at': '2023-10-30T12:00:00'
        }
        review = Review(**review_data)
        self.assertEqual(review.id, '789')
        self.assertEqual(review.place_id, place_id)
        self.assertEqual(review.user_id, user_id)
        self.assertEqual(review.text, text)
        self.assertEqual(review.created_at, datetime.strptime('2023-10-29T12:00:00', Review.DATE_FORMAT))
        self.assertEqual(review.updated_at, datetime.strptime('2023-10-30T12:00:00', Review.DATE_FORMAT))


if __name__ == '__main__':
    unittest.main()
