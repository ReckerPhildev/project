from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Speedy(models.Model):
    name=models.CharField(max_length=40, unique=True)
    description = models.CharField(max_length=100)
    def _str_(self):
        return self.name

class Post(models.Model):
    message=models.TextField(max_length=5000)
    speedy=models.ForeignKey(Speedy,on_delete=models.CASCADE,related_name='posts')
    created_at=models.DateTimeField(null=True)
    last_updated=models.DateTimeField(auto_now_add=True)
    starter=models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts')

class comment(models.Model):
    message=models.TextField(max_length=5000)
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comment')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(null=True)
    created_at=models.ForeignKey(User, on_delete=models.CASCADE,related_name='comment')
    updated_by=models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='+')
