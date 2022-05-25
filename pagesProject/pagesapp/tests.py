from urllib import response
from django.test import TestCase, SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_home_page_st_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_st_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_contact_page_st_code(self):
        response=self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)


# Create your tests here.
