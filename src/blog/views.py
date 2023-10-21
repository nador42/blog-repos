from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from .models import BlogPost


# Create your views here.

def blog_posts(request):
    #return HttpResponse("home")
    #return redirect("https://www.google.fr")
    #blog_post=get_object_or_404(BlogPost,pk=3)
    #posts=BlogPost.objects.filter(pk__in=[10,12,13])
    posts=BlogPost.objects.all()
    return render(request,"blog/post.html",context={"posts":posts})
    #return render(request,"blog/post.html",context={"blog_post":blog_post})

def index(request):
    return HttpResponse("<h1>Le blog </h1>")


def blog_post(request,pk):
    post = BlogPost.objects.get(pk=pk)
    print(pk)
    return render(request,"blog/post_2.html",context={"post":post})