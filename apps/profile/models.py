from django.db import models


class User(models.Model):
    """This class represents the user model."""
    
    name = models.CharField(max_length=30, default="")
    
    email = models.EmailField(max_length=30, unique=True, primary_key=True,
        db_index=True)
    
    creation_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = (('email'),)
    
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
