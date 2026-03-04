from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(unique=True, max_length=200)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
     post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
     name=models.CharField(max_length=200)
     body=models.TextField()
     created_at=models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
         return f"{self.name} on {self.post.title}"