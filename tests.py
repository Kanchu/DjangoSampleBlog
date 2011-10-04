import unittest
from django.test import TestCase

from models import Blog

class BlogTestCase(TestCase):
    def setUp(self):
        self.feed1 = Blog.objects.create(name='abc',feedback='Good')
        self.feed2 = Blog.objects.create(name='def',feedback='Bad')

    def test_Blog(self):
        self.assertEqual(self.feed1.name,'abc')
        self.assertEqual(self.feed2.name,'def')


if __name__ == '__main__':
    unittest.main()