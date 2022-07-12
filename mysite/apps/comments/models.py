from django.db import models
from django.utils import timezone

from mysite.core.core import foo


class Comment(models.Model):
    post = models.ForeignKey('blogs.Post', on_delete=models.CASCADE, related_name='comments',
                             blank=True, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.text

    def get_foo(self) -> str:
        return foo()
