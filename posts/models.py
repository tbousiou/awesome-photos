from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

# Post model with title, image, body, created_at
class Post(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120, null=True)
    source_url = models.URLField(max_length=300, null=True)
    image_url = models.URLField(max_length=300)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)
    icon = models.FileField(upload_to='icons/', null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if not self.slug:  # Check if the slug is not already set
    #         self.slug = slugify(self.name)  # Generate slug from name
    #     super(Tag, self).save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.name
    

# Model for the post comments
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        try:
            return f"{self.author.username} : {self.body[:30]}"
        except:
            return f"Anonymous : {self.body[:30]}"