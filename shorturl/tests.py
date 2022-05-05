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


# views test
class HomePageTests(SimpleTestCase):

    """check that the HTTP status code for the homepage equals 200"""
    def setUp(self) -> None:
        url = reverse('shorturl:home')
        self.response = self.client.get(url)

    def test_homepage_stats_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'shorturl/home.html')

    def test_homepage_contaons_correct_html(self):
        self.assertContains(self.response, 'Home')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Acceuil')

    # need fix
    # def test_homepage_url_resolves_homepageview(self):
    #     view = resolve('/')
    #     self.assertEqual(view.func.__name__,views.home(request).resolver_match)


# choose_url view
class ChooseUrlNameTests(TestCase):
        
    def test_valid_form(self):
        form_data = {'url_long': 'longurlpourfaireletest', 'url_custom': 'custom',}
        form = ChooseURLNameForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    # def test_choose_url_name(self):
    #     form = ChooseURLNameForm(data={"url_long": "unurlvraimenttreslong", "url_custom": "unurlcustom"})
    #     self.assertEqual(form.errors["#"])

    # test a post data
    def test_post_choose_url_name_form(self):
        form_data = {'url_long': 'longurlpourfaireletest', 'url_custom': 'custom'}
        response = self.client.post('/choose/', data=form_data)
        self.assertEqual(URL.objects.count(), 1)

    # test choose_url template
    def test_choose_url_template(self):
        url = reverse('shorturl:choose_url')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'shorturl/choose_url_name.html')


# hash_url view
class HashUrlTests(TestCase):

    def test_hash_url_template(self):
        url = reverse('shorturl:hash_url')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'shorturl/hash_url.html')

    def test_valid_form(self):
        form_data = {'url_long': 'longurlpourfaireletest', 'url_custom': 'custom',}
        form = HashURLNameForm(data=form_data)
        self.assertTrue(form.is_valid())

    # def test_post_hash_url_form(self):
    #     form_data = {'url_long': 'longurlpourfaireletest', 'url_custom': 'custom',}
    #     response = self.client.post('/hash/', data=form_data)
    #     self.assertEqual(URL.objects.count(), 1)
