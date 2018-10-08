from django.views.generic import TemplateView
from rest_framework import generics
from apps.profile.serializers import UserSerializer
from apps.profile.models import User

class CreateUser(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    # The ListCreateAPIView is a generic view which provides GET (list all)
    # and POST method handlers
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new user."""
        serializer.save()
    
    

class AccountView ( TemplateView ):
    template_name = "profile/account.html"
