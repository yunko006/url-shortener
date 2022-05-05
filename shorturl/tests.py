from urllib import request
from django.test import SimpleTestCase, TestCase

from shorturl import views
from .models import URL
from django.urls import resolve, reverse
from .forms import *


# models test
class URLTest(TestCase):

    def create_url(self, url_long="test avec un url long", url_custom='custom name'):
        return URL.objects.create(url_long=url_long, url_custom=url_custom)

    def test_url_creation(self):
        u = self.create_url()
        self.assertTrue(isinstance(u, URL))
        self.assertEqual(u.__str__(), u.url_custom)
