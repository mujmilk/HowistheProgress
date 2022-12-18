#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app.models import Post
#from django.http import HttpResponse

class PostList(ListView):
    model = Post
    context_object_name = "posts"

class PostDetail(DetailView):
    model = Post
    context_object_name = "post"

# Create your views here.
#def index(request):
#    return HttpResponse('test')
