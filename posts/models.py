from django.db import models
from django.utils.text import slugify

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