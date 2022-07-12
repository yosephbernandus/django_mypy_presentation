from django import forms

from mysite.apps.blogs.models import Post
from mysite.apps.comments.models import Comment
from typing import Any


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(), required=False)

    def __init__(self, post: Post, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.post = post

    def save(self) -> Comment:
        comment = self.post.comments.create(text=self.cleaned_data['text'])
        return comment
