from django.test import TestCase

from apps.profile.models import User


class UserModelTestCase(TestCase):
    """This class defines the test suite for the User model."""
    
    def setUp(self):
        """Define the test client and other test variables."""
        self.user_name = "Name"
        self.user_email = "name@gmail.com"
        self.user = User(name=self.user_firstname, email=self.user_email)
    
    def test_model_can_create_a_user(self):
        """Test the user model can create a user."""
        old_count = User.objects.count()
        self.user.save()
        new_count = User.objects.count()
        self.assertEqual(old_count + 1, new_count)
