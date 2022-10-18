from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.


class URLTests(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_clicked_signup(self):
        response = self.client.get('/clicked_signup')
        self.assertEqual(response.status_code, 200)

    def test_studentsignup(self):
        response = self.client.get('/studentsignup')
        self.assertEqual(response.status_code, 200)

    def test_teachersignup(self):
        response = self.client.get('/teachersignup')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 200)

    def test_aboutus(self):
        response = self.client.get('/aboutus')
        self.assertEqual(response.status_code, 200)

    def test_send_email(self):
        response = self.client.get('/send_email/')
        self.assertEqual(response.status_code, 200)
