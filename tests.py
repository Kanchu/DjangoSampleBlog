import unittest
from django.test import TestCase, Client

from models import Blog

class BlogTestCase(TestCase):
    def setUp(self):
        self.feed1 = Blog.objects.create(name='abc',feedback='Good')
        self.feed2 = Blog.objects.create(name='def',feedback='Bad')

    def test_Blog(self):
        self.assertEqual(self.feed1.name,'abc')
        self.assertEqual(self.feed2.name,'def')

#         needs to instantiate the test client:
class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home(self):
        response = self.client.get('/home')
        self.assertContains(response,'Home Page')

    def test_add(self):
        response = self.client.get('/add',{'var1':'4','var2':'3','opr': 'add'})
        self.assertContains(response,'Addition of 4 and 3 is 7')

        response = self.client.get('/add',{'var1':'abc','var2':'3','opr': 'add'})
        self.assertContains(response,'Invalid Input Numbers!!!')

        response = self.client.get('/add',{'var1':'4','var2':'3','opr': 'sub'})
        self.assertContains(response,'Subtraction of 4 and 3 is 1')


if __name__ == '__main__':
    unittest.main()