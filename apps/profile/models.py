from django.db import models


class User (models.Model):
    """This class represents the user model."""
    name = models.CharField(
        max_length=30
    )

    email = models.EmailField(
        max_length=30,
        unique=True
    )

    creation_time = models.DateTimeField(
        auto_now_add=True
    )
    
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

