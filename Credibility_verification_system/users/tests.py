from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class RegistrationTestCase(TestCase):
    def test_user_registration(self):
        # Define registration form data (adjust as needed)
        registration_data = {
            'Firstname': 'derrick',
            'Lastname': 'nyaga',
            'Username': 'nyaga7',
            'Email': 'derricknyaga007@gmail.com',
            'Password': 'testpassword',
            'Retype_password': 'testpassword',
        }

        # Send a POST request to the registration view
        response = self.client.post(reverse('register'), data=registration_data)

        # Check if the registration was successful (you can customize this based on your project's behavior)
        self.assertEqual(response.status_code, 200)  # Check for a successful registration status code

        # Check if the user was created in the database
        user = User.objects.get(username='nyaga7')  # Retrieve the user from the database
        self.assertIsNotNone(user)  # Check if the user exists in the database

        # Check if user attributes match the registration data
        self.assertEqual(user.first_name, 'derrick')
        self.assertEqual(user.last_name, 'nyaga')
        self.assertEqual(user.email, 'derricknyaga007@gmail.com')
