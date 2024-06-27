from django.db import models

# Create your models here.

# Post model with title, image, body, created_at
class Post(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120, null=True)
    source_url = models.URLField(max_length=300, null=True)
    image_url = models.URLField(max_length=300)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']