from django.db import models
from django.utils import timezone


class Comment(models.Model):
    blogs = models.ForeignKey('blogs.Blog', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.id
