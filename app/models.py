from django.db import models

class Article(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return f"{ self.author } - { self.title }"
