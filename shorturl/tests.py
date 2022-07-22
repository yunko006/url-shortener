from urllib import request
from django.db import IntegrityError
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

    # def test_invalid_form(self):
    #     # w = Whatever.objects.create(title='Foo', body='')
    #     # data = {'title': w.title, 'body': w.body,}
    #     # form = WhateverForm(data=data)
    #     # self.assertFalse(form.is_valid())

    #     test = URL.objects.create(url_long='urllong', url_custom='custom')
    #     test2 = URL.objects.create(url_long='urllong', url_custom='c')
    #     data = {"url_long": test2.url_long, 'custom': test2.url_custom}
    #     form = ChooseURLNameForm(data=data)
    #     self.assertRaises(IntegrityError, test, test2)


# retrieve_url view
class RetrieveUrlTests(TestCase):
    # def setUp(self) -> None:
    #     # URL.objects.create(url_long = 'unurlvraiimentvraimentreslong')
    #     session = self.client.session
    #     session['long_url_existe_deja'] = 'unurlvraiimentvraimentreslong'
    #     session.save()

    # def test_hash_url_template(self):
    #     url = reverse('shorturl:retrieve_url')
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response, 'shorturl/retrieve_url.html')

    # def setUp(self) -> None:
    #     session = self.client.session
    #     session['long_url_existe_deja'] = 'unurlvraiimentvraimentreslong'
    #     session.save()
    #     url = reverse('shorturl:retrieve_url')
    #     self.response = self.client.get(url)
        

    # def test_retrieve_page_stats_code(self):
    #     self.assertEqual(self.response.status_code, 200)

    # def test_retrieve_page_template(self):
    #     self.assertTemplateUsed(self.response, 'shorturl/retrieve_url.html')

    # def test_homepage_contaons_correct_html(self):
    #     self.assertContains(self.response, 'Voici')

    # def test_homepage_does_not_contain_incorrect_html(self):
    #     self.assertNotContains(self.response, 'Hello')
    pass

# hash_url view
class GenerateUrlTests(TestCase):
    def setUp(self) -> None:
        # URL.objects.create(url_long = 'unurlvraiimentvraimentreslong')
        session = self.client.session
        session['long_url_existe_deja'] = 'test'
        session.save()

    def test_hash_url_template(self):
        url = reverse('shorturl:generate_url')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'shorturl/generate_url.html')

    def test_valid_form(self):
        form_data = {'url_long': 'longurlpourfaireletest', 'url_custom': "URL.objects.get(url_long = 'unurlvraiimentvraimentreslong').create_short_url()"}
        form = HashURLNameForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_post_generate_url_name_form(self):
        form_data = {'url_long': 'longurlpourfaireletest', 'url_custom': 'custom'}
        response = self.client.post('/generate/', data=form_data)
        self.assertEqual(URL.objects.count(), 1)

# redirect_url view
class RedirectUrlTests(TestCase):
    """
    Test si l'objet existe : si oui et si non
    Test que le redirect marche bien, response 200
    Test le template
    """
    def setUp(self) -> None:
        URL.objects.create(url_long = 'unurlvraiimentvraimentreslong',url_custom = 'custom')

    def test_object_exist(self):
        # url = URL.objects.get(url_long = 'unurlvraiimentvraimentreslong')
        self.assertEqual(URL.objects.count(), 1)

    def test_redirect_code(self):
        pass

    def test_redirect_is_working(self):
        pass
