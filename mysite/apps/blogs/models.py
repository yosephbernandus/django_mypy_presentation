from django.conf import settings
from django.db import models
from django.utils import timezone

from mysite.apps.comments.models import Comment

from typing import Union, Optional, Tuple


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self) -> None:
        self.published_date = timezone.now()
        self.save()

    def __str__(self) -> str:
        return self.title

    def get_first_comment(self) -> Comment:
        return Comment.objects.filter(post=self).first()

    def get_union_data(self, is_valid: bool = True) -> Union[str, str]:
        if is_valid:
            return 1
        else:
            return 'Not valid'

    def get_optional_data(self, is_valid: bool = True) -> Optional[str]:
        if not is_valid:
            return None

        return 'valid'

    def get_tuple_data(self) -> Tuple:
        return (1, 2, 3)
