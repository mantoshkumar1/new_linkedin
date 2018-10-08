from rest_framework import serializers

from apps.profile.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = User
        fields = ('name', 'email', 'creation_time')
        read_only_fields = ('creation_time',)
