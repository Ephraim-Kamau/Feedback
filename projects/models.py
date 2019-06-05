from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete = models.CASCADE, null=True)
    full_name = models.TextField(max_length=200)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to = 'images/')
    
    def save_profile(self):
        self.save() 

    def delete_profile(self):
        self.delete() 

class Topics(models.Model):
    title=models.TextField(max_length=100)
    description=models.TextField()
    profile = models.ForeignKey(User, on_delete = models.CASCADE, null=True)    
    image_header=models.ImageField(upload_to = 'images/')   


    def save_topics(self):
        self.save() 

    def delete_topics(self):
        self.delete()     