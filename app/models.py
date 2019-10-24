from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return f"{ self.author } - { self.title }"
