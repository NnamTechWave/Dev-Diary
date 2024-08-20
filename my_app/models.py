from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now=True)
    # created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(blog, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    
class personal_detail(models.Model):
    full_name = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/')

class Meta:
    db_table = "personal_detail"

    