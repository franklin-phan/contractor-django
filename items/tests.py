import unittest

from django.test import TestCase, Client
from django.contrib.auth.models import User
from items.models import Page

# Create your tests here.

class BlogTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests that True equals True. """
        self.assertEqual(True, True)

    def test_page_slugify_on_save(self):
        """ Test if we generate the proper slug. """
        user = User()
        user.save()

        page = Page(title="My Test Page", content="Test", author=user)
        page.save()

        page1 = Page(title="My Second - / Test Page", content="secont test", author=user)
        self.assertEqual(page.slug, "my-test-page")

class PageListViewTests(TestCase):
    """ tests that the homepage works. """

    def test_multiple_pages(self):

        #create a user
        user = User.objects.create()

        Page.objects.create(title="My test page.", content="test", author=user)
        Page.objects.create(title="My test page 2.", content="test", author=user)

        # getting the home route
        response = self.client.get('/')

        # page found, status code 200
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.context['all_pages']), 2)

    def test_multiple_pages_response(self):

         #create a user
        user = User.objects.create()

        Page.objects.create(title="My test page.", content="test", author=user)
        Page.objects.create(title="My test page 2.", content="test", author=user)

        # getting the home route
        response = self.client.get('/')
        responses = response.context['all_pages']

        self.assertQuerysetEqual(
            responses,
            ['<Page: My test page.>', '<Page: My test page 2.>'],
            ordered=False
        )

class NewPageTests(TestCase):
    """ Test Blog submission """
    def setUp(self):
        user = User.objects.create()

        Page.objects.create(title="My test page.", content="test", author=user)
        Page.objects.create(title="My test page 2.", content="test", author=user)

        # getting the home route
        self.my_response = self.client.get('/submit')
        
    def test_page_load(self):
        self.assertEqual(self.my_response.status_code, 301)