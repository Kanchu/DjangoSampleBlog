import unittest
from django.test import TestCase

from models import Blog

class BlogTestCase(TestCase):
    def setUp(self):
        self.feed1 = Blog.objects.create(name='abc',feedback='Good')
        self.feed2 = Blog.objects.create(name='def',feedback='Bad')

    def test_Blog(self):
        self.assertEqual(self.feed1.name,'abc')
        self.assertEqual(self.feed2.name,'abc')

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 2, 2)

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

if __name__ == '__main__':
    unittest.main()