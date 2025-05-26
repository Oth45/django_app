from django.conf import settings
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)  
    content = models.TextField()             
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  # Display title in admin panel

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username