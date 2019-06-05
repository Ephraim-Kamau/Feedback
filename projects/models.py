from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete = models.CASCADE, null=True)
    full_name = models.TextField(max_length=200)
    email = models.EmailField()

    def save_profile(self):
        self.save() 

    def delete_profile(self):
        self.delete() 