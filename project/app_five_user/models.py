from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=50, blank=True)
    bio =  models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default="images/profile.png", blank=True)
    email = models.CharField(max_length=50, blank=True)

    def __str__(self) :
        return self.user.username