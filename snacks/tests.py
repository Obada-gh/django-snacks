from django.test import TestCase
from django import urls
from django.test import TestCase , SimpleTestCase
from django.urls import reverse

# Create your tests here.

class Snacks(SimpleTestCase):
    def test_home_status(self):
        url = reverse('home')
        actual = self.client.get(url).status_code
        expected = 200
        self.assertEqual(actual,expected)


    def test_about_status(self):
        url = reverse('about')
        actual = self.client.get(url).status_code
        expected = 200

        self.assertEqual(actual,expected)
    
    def test_template_home(self):
        url=reverse('home')
        actual = self.client.get(url)
        expected= 'home.html'
        self.assertTemplateUsed(actual,expected)
    

    def test_template_about(self):
        url=reverse('about')
        actual = self.client.get(url)
        expected= 'about.html'
        self.assertTemplateUsed(actual,expected)

    
    



    
