from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class UserViewTestCase(TestCase):
    """Test suite for the api views."""
    
    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.user_data = { 'name': 'User Name', 'email': 'test@test.com' }
        self.response = self.client.post(reverse('profile:create'),
                                         self.user_data, format="json")
    
    def test_api_can_create_an_user(self):
        """Test the api has user creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
