from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import Post
import random


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post(request, slug):
    return render_to_response('gvs_post.html',
                              {'post': get_object_or_404(Post, slug=slug)})


def about(request):
    return render_to_response('about.html')


def random_post(request):
    posts = Post.objects.all()
    random_post = random.choice(posts)
    return render_to_response('gvs_post.html',
                              {'post': get_object_or_404(Post, slug=random_post.slug)})
