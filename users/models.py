from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    displayname = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)

    email = models.EmailField(unique=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    @property
    def get_avatar_url(self):
        try:
            avatar = self.avatar.url
        except:
            avatar = static('images/avatar_default.svg')
        return avatar
    
    @property
    def get_name(self):
        if self.displayname:
            name = self.displayname
        else:
            name = self.user.username 
        return name