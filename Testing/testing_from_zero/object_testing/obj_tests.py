import unittest
from object_testing.object_for_testing import Cat
from random import randrange, choice

names = ['Barsik', 'Murzik', 'Pushistik', 'Markiza']


class CatGetOlder(unittest.TestCase):

    def setUp(self):
        self.test_cat = Cat(choice(names), 5)

    def test_age_type(self):
        self.assertIsInstance(self.test_cat.age, int)

    def test_get_older(self):
        self.test_cat.get_older(3)
        self.assertEqual(self.test_cat.age, 8)


    def tearDown(self):
        print(self.test_cat.name)




if __name__ == "__main__":
    unittest.main()