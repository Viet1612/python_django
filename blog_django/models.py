from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    passw = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    
    def __str__(self):
        return self.user_name
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,unique=True)
    contend = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    