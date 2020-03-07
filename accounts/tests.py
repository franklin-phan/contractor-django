from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase

# Create your tests here.
class CreateUserTest(TestCase):
    """ Test if User works """
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.c = Client()
        self.logged_in = self.c.login(username='testuser', password='12345')
    
    def test_user_login(self):
        """ Test if user is logged in"""
        self.assertTrue(self.logged_in)

    def test_login_credential(self):
        """ Test if user has the right credentials """
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.password, '12345')