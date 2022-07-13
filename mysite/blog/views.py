from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from mysite.apps.blogs.models import Post

from mysite.blog.decorators import superuser_required


@superuser_required
def post_list(request: str) -> HttpResponse:
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
